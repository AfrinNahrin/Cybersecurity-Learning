import os
import json

print("=" * 40)
print("        ATM SYSTEM V3")
print("=" * 40)

BASE_DIR = os.path.dirname(__file__)

ACCOUNT_FILE = os.path.join(BASE_DIR, "account.json")
TRANSACTION_FILE = os.path.join(BASE_DIR, "transaction_log.json")

# Load Account Data
with open(ACCOUNT_FILE, "r", encoding="utf-8") as file:
    accounts = json.load(file)

# Load Transaction History
with open(TRANSACTION_FILE, "r", encoding="utf-8") as file:
    transactions = json.load(file)

print("\nFiles Loaded Successfully!")
print(accounts)
print(transactions)


# ==========================
# LOGIN FUNCTION
# ==========================

def login():

    attempts = 3

    while attempts > 0:

        account_number = input("\nEnter Account Number: ")
        pin = input("Enter ATM PIN: ")

        if account_number not in accounts:
            print("Account Not Found!")
            continue

        if accounts[account_number]["pin"] == pin:

            print("\n=========================")
            print("Login Successful!")
            print(f"Welcome {accounts[account_number]['name']}")
            print("=========================")

            return account_number

        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts Left: {attempts}")

    print("\nAccount Locked!")
    return None


# ==========================
# ATM MENU
# ==========================

def show_menu():

    print("\n=========================")
    print("        ATM MENU")
    print("=========================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")

    return input("\nEnter Your Choice: ")


# ==========================
# CHECK BALANCE
# ==========================

def check_balance(current_user):

    print("\n=========================")
    print("      ACCOUNT BALANCE")
    print("=========================")

    balance = accounts[current_user]["balance"]

    print(f"Account Holder : {accounts[current_user]['name']}")
    print(f"Balance        : {balance} TK")

# ==========================
# SAVE ACCOUNT DATA
# ==========================

def save_accounts():

    with open(ACCOUNT_FILE, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)

# ==========================
# SAVE TRANSACTION HISTORY
# ==========================

def save_transactions():

    with open(TRANSACTION_FILE, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)

# ==========================
# RECORD TRANSACTION
# ==========================

def add_transaction(account_number, transaction_type, amount):

    transaction = {
        "account": account_number,
        "type": transaction_type,
        "amount": amount,
        "balance": accounts[account_number]["balance"]
    }

    transactions.append(transaction)

    save_transactions()

# ==========================
# DEPOSIT MONEY
# ==========================

def deposit(current_user):

    print("\n========== DEPOSIT ==========")

    try:
        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        accounts[current_user]["balance"] += amount

        save_accounts()

        add_transaction(current_user, "Deposit", amount)

        print("\nDeposit Successful!")
        print(f"Current Balance: {accounts[current_user]['balance']} TK")

    except ValueError:
        print("Please Enter Numbers Only!")


# ==========================
# WITHDRAW MONEY
# ==========================

def withdraw(current_user):

    print("\n========== WITHDRAW ==========")

    try:
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        current_balance = accounts[current_user]["balance"]

        if amount > current_balance:
            print("Insufficient Balance!")
            return

        accounts[current_user]["balance"] -= amount

        save_accounts()

        add_transaction(current_user, "Withdraw", amount)

        print("\nWithdraw Successful!")
        print(f"Remaining Balance: {accounts[current_user]['balance']} TK")

    except ValueError:
        print("Please Enter Numbers Only!")

# ==========================
# SHOW TRANSACTION HISTORY
# ==========================

def show_history(current_user):

    print("\n========== TRANSACTION HISTORY ==========")

    found = False

    for transaction in transactions:

        if transaction["account"] == current_user:

            print("----------------------------")
            print("Type   :", transaction["type"])
            print("Amount :", transaction["amount"], "TK")
            print("Balance:", transaction["balance"], "TK")

            found = True

    if not found:
        print("No Transactions Found.")

# ==========================
# CHANGE PIN
# ==========================

def change_pin(current_user):

    print("\n========== CHANGE PIN ==========")

    current_pin = input("Enter Current PIN: ")

    if current_pin != accounts[current_user]["pin"]:
        print("Incorrect Current PIN!")
        return

    new_pin = input("Enter New PIN: ")
    confirm_pin = input("Confirm New PIN: ")

    if new_pin != confirm_pin:
        print("PIN Does Not Match!")
        return

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN Must Be Exactly 4 Digits!")
        return

    if new_pin == current_pin:
        print("New PIN Cannot Be Same As Old PIN!")
        return

    accounts[current_user]["pin"] = new_pin

    save_accounts()

    add_transaction(current_user, "PIN Changed", 0)

    print("\nPIN Changed Successfully!")


# ==========================
# MAIN PROGRAM
# ==========================

current_user = login()

if current_user is None:
    exit()

while True:

    choice = show_menu()

    if choice == "1":
        check_balance(current_user)

    elif choice == "2":
        deposit(current_user)

    elif choice == "3":
         withdraw(current_user)

    elif choice == "4":
         show_history(current_user)

    elif choice == "5":
         change_pin(current_user)

    elif choice == "6":
        print("\nThank You For Using Our ATM.")
        break

    else:
        print("\nThis Feature Will Be Added Soon.")