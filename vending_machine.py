class Drink:
    """
    Represents a drink sold by the vending machine.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - R{self.price:.2f}"


class Stock:
    """
    Manages drink quantities in the vending machine.
    """
    def __init__(self):
        self.items = {}

    def add_drink(self, drink, quantity):
        self.items[drink] = quantity

    def is_available(self, drink, quantity=1):
        return self.items.get(drink, 0) >= quantity

    def reduce_stock(self, drink, quantity):
        if self.is_available(drink, quantity):
            self.items[drink] -= quantity

    def display_stock(self):
        print("\nAvailable drinks:")
        for index, drink in enumerate(self.items.keys(), start=1):
            print(f"{index}. {drink} (Stock: {self.items[drink]})")


class VendingMachine:
    """
    Controls vending machine operations and user interaction.
    """
    def __init__(self, stock):
        self.stock = stock
        self.balance = 0.0

    def insert_money(self, amount):
        # 🔴 FIX: Prevent R0 or negative amounts
        if amount <= 0:
            print("Invalid amount. Please insert money greater than R0.")
            return False

        self.balance += amount
        print(f"Current balance: R{self.balance:.2f}")
        return True

    def offer_refund(self):
        choice = input("Would you like your money back? (y/n): ").lower()

        if choice == 'y':
            print(f"Refunding R{self.balance:.2f}")
            self.balance = 0.0
        else:
            print("Balance kept. You may select another drink.")

    def select_drink(self, drink):
        # Drink out of stock
        if not self.stock.is_available(drink):
            print("Sorry, this drink is out of stock.")
            self.offer_refund()
            return

        # Insufficient funds
        if self.balance < drink.price:
            print(f"Insufficient funds. {drink.name} costs R{drink.price:.2f}")
            self.offer_refund()
            return

        # Exact price
        if self.balance == drink.price:
            self.stock.reduce_stock(drink, 1)
            self.balance -= drink.price
            print(f"Dispensing 1 bottle of {drink.name}...")
            self.return_change()
            return

        # More than price
        max_affordable = int(self.balance // drink.price)
        print(f"You can buy up to {max_affordable} bottle(s) of {drink.name}.")

        try:
            quantity = int(input("How many bottles would you like to buy? "))
        except ValueError:
            print("Invalid quantity.")
            self.offer_refund()
            return

        if quantity <= 0:
            print("Quantity must be at least 1.")
            self.offer_refund()
            return

        if not self.stock.is_available(drink, quantity):
            print("Sorry, not enough stock available.")
            self.offer_refund()
            return

        total_cost = drink.price * quantity

        if self.balance < total_cost:
            print("Insufficient balance for that quantity.")
            self.offer_refund()
            return

        self.stock.reduce_stock(drink, quantity)
        self.balance -= total_cost
        print(f"Dispensing {quantity} bottle(s) of {drink.name}...")
        self.return_change()

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: R{self.balance:.2f}")
            self.balance = 0.0

        print("Thank you for your purchase!\n")


# ---------------- Main Program ----------------

coke = Drink("Coke", 25.00)
water = Drink("Water", 8.00)
juice = Drink("Juice", 18.00)

stock = Stock()
stock.add_drink(coke, 10)
stock.add_drink(water, 5)
stock.add_drink(juice, 15)

machine = VendingMachine(stock)

while True:
    stock.display_stock()

    choice = input("\nSelect a drink number (or 'q' to quit): ")

    if choice.lower() == 'q':
        print("Goodbye!")
        break

    try:
        choice = int(choice)
        drinks_list = list(stock.items.keys())
        selected_drink = drinks_list[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        continue

    try:
        amount = float(input("Insert money (R): "))

        # 🔴 If invalid money, restart loop
        if not machine.insert_money(amount):
            continue

        machine.select_drink(selected_drink)

    except ValueError:
        print("Invalid amount.")

