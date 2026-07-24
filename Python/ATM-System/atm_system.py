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

        print("\nDeposit Successful!")
        print(f"Current Balance: {accounts[current_user]['balance']} TK")

    except ValueError:
        print("Please Enter Numbers Only!")


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

    elif choice == "6":
        print("\nThank You For Using Our ATM.")
        break

    else:
        print("\nThis Feature Will Be Added Soon.")