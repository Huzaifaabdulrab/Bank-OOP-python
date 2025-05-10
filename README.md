# Bank Account Management System

This is a Python-based Bank Account Management System that leverages Object-Oriented Programming (OOP) principles. The system provides functionalities such as account creation, deposits, withdrawals, transfers, and balance checks, while ensuring data security and organization through encapsulation and abstraction.

## Features

- **User Account Creation**: Users can create a secure account by setting a unique pin and username.
- **Deposit**: Users can deposit money into their accounts, and their balance is updated accordingly.
- **Transfer**: Allows users to transfer funds to other accounts with balance checks.
- **Withdrawal**: Users can withdraw funds while ensuring they have enough balance.
- **Balance Inquiry**: Check the current account balance at any time.
- **Exit** : Exit program close bank

## Key Concepts Used

- **Encapsulation**: Sensitive data (like user details, pin, and transactions) are encapsulated within the `Bank` class.
- **Initialization**: Account data such as username, pin, and initial balance is initialized at account creation.
- **Abstraction**: Complex banking processes (deposit, transfer, etc.) are abstracted behind simple function calls, making the system user-friendly.

## File Structure

- **userdata.json**: Stores user data (username, pin, and transaction history).
- **main.py**: Contains the logic for account creation, transactions, and balance management.

## Requirements

- Python 3.x or higher.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Huzaifaabdulrab/Bank-OOP-python
