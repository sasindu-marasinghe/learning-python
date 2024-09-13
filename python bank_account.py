# Bank Account Management System using OOP

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero!")
            return
        self.balance += amount
        print(f"\n{amount} has been deposited into {self.owner}'s account.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return
        if amount > self.balance:
            print(f"\nInsufficient funds! {self.owner} has only {self.balance} in the account.")
            return
        self.balance -= amount
        print(f"\n{amount} has been withdrawn from {self.owner}'s account.")
    
    def check_balance(self):
        print(f"\n{self.owner}'s account balance is: {self.balance}\n")

# Function to display the menu
def display_menu():
    print("\nBank Account Management System")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

# Main program
def main():
    # Creating an account for the user
    owner = input("Enter the account owner's name: ")
    account = BankAccount(owner)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print(f"\nThank you for using the Bank Account Management System. Goodbye, {account.owner}!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
