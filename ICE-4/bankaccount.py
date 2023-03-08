#Create a class and define the functions
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

#Create deposit function
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

#Create withdraw function
    def withdraw(self, amount):
        if self.balance < amount:
            print("Withdrawal failed. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

#Create function for displaying balance
    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Account number: {self.account_number}")
        print(f"Current balance: {self.balance}")

#define a function to create an account
def create_account():
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    balance = float(input("Enter starting balance: "))
    account = BankAccount(account_number, account_holder, balance)
    return account

#define main function
def main():
    accounts = []
    while True:
        print("\n1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            account = create_account()
            accounts.append(account)
            print("Account created successfully!")
            
        elif choice == "2":
            account_number = input("Enter account number: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found!")
            
        elif choice == "3":
            account_number = input("Enter account number: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found!")
            
        elif choice == "4":
            account_number = input("Enter account number: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                account.display_balance()
            else:
                print("Account not found!")
            
        elif choice == "5":
            print("Thank you. Have a good day!")
            break
        
        else:
            print("Invalid. Please try again.")


if __name__ == '__main__':
    main()