Vending Machine – Object-Oriented Programming Assignment
Overview

This project is a command-line vending machine simulation written in Python, designed to demonstrate object-oriented programming (OOP) principles.
The program allows users to select drinks, insert money, purchase single or multiple items, receive change, and request refunds when transactions cannot be completed.

No graphical interface is used; all interaction happens through the terminal.

Objectives of the Assignment

Practice object-oriented design

Use multiple classes with clear responsibilities

Simulate real-world vending machine behavior

Write readable, well-structured, and commented code

Classes and Responsibilities
1. Drink

Responsibility:
Represents a product sold by the vending machine.

Why this class exists:

Encapsulates drink-related data (name and price)

Makes it easy to add new products in the future

Key attributes:

name: Name of the drink

price: Cost of the drink

2. Stock

Responsibility:
Manages inventory and availability of drinks.

Why this class exists:

Separates stock management from vending logic

Centralizes stock checks and updates

Key features:

Stores drinks and their quantities

Checks availability before dispensing

Reduces stock after a successful purchase

Displays available drinks to the user

3. VendingMachine

Responsibility:
Controls the vending machine’s behavior and user interaction.

Why this class exists:

Acts as the “brain” of the system

Handles money, purchases, refunds, and user decisions

Key features:

Accepts and validates money input

Prevents invalid amounts (e.g. R0 or negative values)

Handles exact payment and excess payment

Allows bulk purchases when the user inserts more money

Offers refunds when:

The selected drink is out of stock

The balance is insufficient

An invalid quantity is entered

Returns change after dispensing

How the Classes Interact

The main program displays available drinks using Stock

The user selects a drink

The user inserts money

VendingMachine:

Validates the money

Checks availability using Stock

Determines whether the user can buy one or multiple items

Stock updates quantities after dispensing

VendingMachine returns change or refunds money if needed

This separation ensures low coupling and high cohesion, which are core OOP principles.

Key Features Implemented

Multiple drinks with different prices

Stock tracking per drink

Validation of user input

Exact payment handling

Bulk purchasing (when extra money is inserted)

Refund option when:

Drink is unavailable

Funds are insufficient

Change returned after purchase

R0 and negative amounts rejected as invalid

Assumptions and Simplifications

The machine only accepts one money insertion per transaction

Currency is assumed to be South African Rand (R)

No persistent storage (stock resets when the program restarts)

No authentication or admin mode

Terminal-based interface only

These choices were made to keep the focus on OOP design rather than UI or databases.

Error Handling

Invalid drink selection is handled gracefully

Invalid money input (non-numeric, zero, or negative) is rejected

Invalid quantity input triggers a refund option

Out-of-stock scenarios do not trap user money

Possible Improvements and Extensions

If more time were available, the system could be extended by:

Allowing multiple money insertions before selecting a drink

Adding a refill/admin mode

Saving stock data to a file or database

Adding snack categories

Implementing unit tests

Creating a GUI or web interface

Conclusion

This project demonstrates a clear understanding of:

Object-oriented programming concepts

Class responsibility separation

Real-world problem modeling

User input validation and error handling

The solution focuses on clarity, realism, and maintainability, rather than complexity.
