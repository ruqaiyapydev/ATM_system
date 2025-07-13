# # BASE ATM Project

# balance = 5000  # Starting balance
# pin = "1234"    # Simple pin

# # Step 1: PIN Verification
# entered_pin = input("Enter your ATM PIN: ")

# if entered_pin == pin:
#     print("Welcome Ruqaiya Queen! 💙")
    
#     while True:
#         print("\n=== ATM MENU ===")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")

#         choice = input("Select option (1-4): ")

#         if choice == "1":
#             print("Your balance is:", balance)

#         elif choice == "2":
#             amount = float(input("Enter amount to deposit: "))
#             balance += amount
#             print("New balance is:", balance)

#         elif choice == "3":
#             amount = float(input("Enter amount to withdraw: "))
#             if amount > balance:
#                 print("Insufficient funds Ruqaiya!")
#             else:
#                 balance -= amount
#                 print("Withdrawal successful. New balance:", balance)

#         elif choice == "4":
#             print("Thank you Ruqaiya Queen! 💙")
#             break

#         else:
#             print("Invalid option, please try again.")

# else:
#     print("Incorrect PIN. Access Denied.")



# import os

# # File name
# balance_file = "balance.txt"

# # Check if file exists
# if os.path.exists(balance_file):
#     with open(balance_file, "r") as file:
#         balance = float(file.read())
# else:
#     balance = 5000  # Default balance

# pin = "1234"

# entered_pin = input("Enter your ATM PIN: ")

# if entered_pin == pin:
#     print("Welcome Ruqaiya Queen! 💙")

#     while True:
#         print("\n=== ATM MENU ===")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")

#         choice = input("Select option (1-4): ")

#         if choice == "1":
#             print("Your balance is:", balance)

#         elif choice == "2":
#             amount = float(input("Enter amount to deposit: "))
#             balance += amount
#             print("New balance is:", balance)

#         elif choice == "3":
#             amount = float(input("Enter amount to withdraw: "))
#             if amount > balance:
#                 print("Insufficient funds Ruqaiya!")
#             else:
#                 balance -= amount
#                 print("Withdrawal successful. New balance:", balance)

#         elif choice == "4":
#             # SAVE BALANCE BEFORE EXIT
#             with open(balance_file, "w") as file:
#                 file.write(str(balance))
#             print("Balance saved! Thank you Ruqaiya Queen! 💙")
#             break

#         else:
#             print("Invalid option, please try again.")

# else:
#     print("Incorrect PIN. Access Denied.")


import os

# File name
balance_file = "balance.txt"

# Check if file exists
if os.path.exists(balance_file):
    with open(balance_file, "r") as file:
        balance = float(file.read())
else:
    balance = 5000  # Default balance

pin = "1234"

entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    print("Welcome Ruqaiya Queen! 💙")

    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select option (1-4): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("New balance is:", balance)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds Ruqaiya!")
            else:
                balance -= amount
                print("Withdrawal successful. New balance:", balance)

        elif choice == "4":
            # SAVE BALANCE BEFORE EXIT
            with open(balance_file, "w") as file:
                file.write(str(balance))
            print("Balance saved! Thank you Ruqaiya Queen! 💙")
            break

        else:
            print("Invalid option, please try again.")

else:
    print("Incorrect PIN. Access Denied.")



# Multiple Users ATM

users = {
    "1234": 5000,
    "5678": 7000,
    "9999": 10000
}

entered_pin = input("Enter your ATM PIN: ")

if entered_pin in users:
    print("Welcome Ruqaiya Queen! 💙")
    balance = users[entered_pin]

    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select option (1-4): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("New balance is:", balance)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print("Withdrawal successful. New balance:", balance)

        elif choice == "4":
            users[entered_pin] = balance  # Update balance in dict
            print("Thank you Ruqaiya Queen! 💙")
            break

        else:
            print("Invalid option, please try again.")

else:
    print("Incorrect PIN. Access Denied.")




import json

# File name
file_name = "users.json"

# Step 1: If file exists, load users; else, create default users
try:
    with open(file_name, "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {
        "1234": 5000,
        "5678": 7000,
        "9999": 10000
    }

entered_pin = input("Enter your ATM PIN: ")

if entered_pin in users:
    print("Welcome Ruqaiya Queen! 💙")
    balance = users[entered_pin]

    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select option (1-4): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("New balance is:", balance)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print("Withdrawal successful. New balance:", balance)

        elif choice == "4":
            # Update balance in users dict
            users[entered_pin] = balance
            # Save back to file
            with open(file_name, "w") as file:
                json.dump(users, file)
            print("Balance saved! Thank you Ruqaiya Queen! 💙")
            break

        else:
            print("Invalid option, please try again.")

else:
    print("Incorrect PIN. Access Denied.")




import json

class ATM:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open(self.file_name, "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {"1234": 5000, "5678": 7000, "9999": 10000}

    def login(self, pin):
        if pin in self.users:
            print("Welcome Queen Ruqaiya! 💙")
            self.current_pin = pin
            self.balance = self.users[pin]
            return True
        else:
            print("Invalid PIN!")
            return False

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited. New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print("Withdrawal successful. New balance:", self.balance)

    def save_balance(self):
        self.users[self.current_pin] = self.balance
        with open(self.file_name, "w") as file:
            json.dump(self.users, file)
        print("Balance saved! Thank you Ruqaiya! 💙")

# Run
atm = ATM("users.json")
pin = input("Enter your PIN: ")
if atm.login(pin):
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Select (1-4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amt = float(input("Amount to deposit: "))
            atm.deposit(amt)
        elif choice == "3":
            amt = float(input("Amount to withdraw: "))
            atm.withdraw(amt)
        elif choice == "4":
            atm.save_balance()
            break
        else:
            print("Invalid option.")

