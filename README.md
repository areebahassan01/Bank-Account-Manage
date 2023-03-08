# Bank Account Management System
This is a bank account management system implemented in Python using object-oriented programming concepts. The system allows users to create accounts, deposit money, withdraw money, and check their account balance.

# Class Definition
BankAccount
This is the main class that represents a bank account. It has the following attributes:

account_number - The unique identifier for the account
account_holder - The name of the account holder
balance - The current balance of the account (default: 0)

The class has the following methods:

deposit(self, amount) - Method for depositing money into the account
withdraw(self, amount) - Method for withdrawing money from the account
display_balance(self) - Method for displaying the current balance of the account

# Functions
create_account()
This function allows users to create a new bank account. It prompts the user for the account number, account holder name, and starting balance. It then creates a new BankAccount object with the provided information and returns it.

main()
This is the main function of the program. It creates an empty list of accounts and enters a loop that prompts the user to select an action (create account, deposit, withdraw, check balance, or exit). Depending on the user's choice, it either calls the appropriate function or prints an error message if the account number is not found.

# How to use
Enter any options from 1-5 in the terminal of the IDE.
When you enter 1, the screen will pop up and you will have to create an account.
When you enter 2, you will be asked to enter the account number, if the account number exists you will have to enter the amount to deposit.
When you enter 3, you will enter the amount to withdraw.
When you enter 4, the balance will be displayed.
When you enter 5, the loop will terminate.
If you enter any number other than from 1 to 5, you will get an error.

# Running the Program
To run the program,  run the main() function. Type bankaccount.py in the terminal of the IDE. This will start the program and allow the user to interact with the bank account management system.
