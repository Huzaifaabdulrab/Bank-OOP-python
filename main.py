import os
import json

class Bank():
    def __init__(self):
        # Initialize file path and other attributes
        self.file_path = "userdata.json"  # Path to the user data file
        self.user_name = self.get_user_name()  # Prompt for user name
        self.__user_pin = self.get_user_pin()  # Prompt for user pin (private)
        self.user_balance = self.get_user_balance()  # Initialize balance to 0
        self.greet_user()  # Greet the user
        self.payment_methods = self.show_payment_methods()  # Show available payment methods
        self.save_user_data()  # Save user data to the file

    def get_user_name(self):
        """Prompt user to enter their name."""
        while True:
            name = input("Hii, what is your name? Your name is very important as it helps set up your account : ")
            if name:
                return name.title()  # Return formatted name
            else:
                print("Please enter a valid name")

    def get_user_pin(self):
        """Prompt user to set up a pin."""
        while True:
            try:
                user_pin = int(input("Write your account pin (make sure it's secret, don't tell anyone): "))
                if user_pin >= 5:
                    return user_pin  # Ensure pin is at least 5 digits long
                else:
                    print("Your pin should be at least 5 digits long")
            except ValueError:
                print("Invalid input, please enter a number")

    def greet_user(self):
        """Display a greeting message to the user."""
        print(f"Hello, {self.user_name.title()}! Welcome to Huzaifa Abdulrab bank system")
        print(f"Dear {self.user_name.title()}! Your current balance is {self.user_balance}")
        
    def save_user_data(self):
        """Save user data to a JSON file."""
        user_data = {
            "user_name": self.user_name,
            "user_pin": self.__user_pin,
            "transactions": []  # Initialize transactions list
        }

        # Check if file exists and load data, otherwise initialize an empty list
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []  # Handle case where file is empty or corrupted
        else:
            data = []  # Initialize empty data if file doesn't exist

        # Check if user already exists in the data file
        for user in data:
            if user["user_name"] == self.user_name and user["user_pin"] == self.__user_pin:
                print("⚠️ User already exists. Continuing with existing data...")
                return  # Exit if user already exists

        # Add the new user's data to the list and save it
        data.append(user_data)
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)  # Save data in JSON format with indentation

    def log_activity(self, action, amount=0):
        """Log the user's activity (Deposit, Transfer, Withdraw) in the transaction history."""
        # Load the existing data
        with open(self.file_path, "r") as file:
            data = json.load(file)

        # Find the user and append the transaction activity
        for user in data:
            if user["user_name"] == self.user_name and user["user_pin"] == self.__user_pin:
                user["transactions"].append({
                    "action": action,
                    "amount": amount,
                    "balance_after": self.user_balance
                })

        # Save the updated data back to the file
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def get_user_balance(self):
        """Initialize user balance. (Currently set to 0)"""
        return 0  # Default balance set to 0

    def show_payment_methods(self):
        """Display the available payment methods to the user."""
        print("💳 Available Payment Methods:")
        methods = [
            "1. Deposit",
            "2. Transfer",
            "3. Withdrawal",
            "4. Total Balance",
            "5. Exit"
        ]
        for method in methods:
            print(method)

        while True:
            choice = input("\nEnter the number of the method you want to use: ")
            if choice == '1':  # Deposit method
                try:
                    deposit_amount = int(input("Enter your deposit amount: "))
                    self.user_balance += deposit_amount  # Add deposit to balance
                    print(f"Your new balance is {self.user_balance}")
                    self.log_activity("Deposit", deposit_amount)  # Log activity
                except ValueError:
                    print("Invalid input, please enter a number")
            elif choice == '2':  # Transfer method
                try:
                    transfer_amount = int(input("Enter the amount you want to transfer: "))
                    if transfer_amount >= self.user_balance:
                        print("Insufficient balance")
                    else:
                        self.user_balance -= transfer_amount  # Subtract transfer amount from balance
                        print(f"Your new balance is {self.user_balance}")
                        self.log_activity("Transfer", transfer_amount)  # Log activity
                except ValueError:
                    print("Invalid input, please enter a number")
            elif choice == '3':  # Withdrawal method
                try:
                    if self.user_balance == 0:
                        print("Insufficient balance")
                    else:
                        withdraw_amount = int(input("Enter the amount you want to withdraw: "))
                        if self.user_balance >= withdraw_amount:
                            self.user_balance -= withdraw_amount  # Subtract withdrawal amount from balance
                            print(f"Your new balance is {self.user_balance}")
                            self.log_activity("Withdraw", withdraw_amount)  # Log activity
                        else:
                            print("You don't have enough balance for this withdrawal.")
                except ValueError:
                    print("Invalid input, please enter a number")
            elif choice == '4':  # View current balance
                print(f"Your current balance is {self.user_balance}")
            elif choice == '5':  # Exit method
                print(f"{self.user_name} Close bank. Thank you for using our Huzaifa Abdulrab services")
                break  # Exit the loop
            else:
                print("Invalid choice")  # Handle invalid input

# Create a bank object and start the process
bank = Bank()
