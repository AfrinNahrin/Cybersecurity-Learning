import os
import json
from datetime import datetime
from utils import print_receipt
from account import (
    login,
    check_balance,
    change_pin,
)
from transaction import (
    deposit,
    withdraw,
    transfer_money,
    show_history,
)

print("=" * 45)
print("      ATM MANAGEMENT SYSTEM V4")
print("=" * 45)

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
    print("6. Transfer Money")
    print("7. Exit")
    

    return input("\nEnter Your Choice: ")

# ==========================
# MAIN PROGRAM
# ==========================

current_user = login(accounts)

if current_user is None:
    exit()

while True:

    choice = show_menu()

    if choice == "1":
        check_balance(accounts, current_user)

    elif choice == "2":
        deposit(
    accounts,
    current_user,
    ACCOUNT_FILE,
    transactions,
    TRANSACTION_FILE,
    BASE_DIR,
    print_receipt,
)

    elif choice == "3":
         withdraw(
    accounts,
    current_user,
    ACCOUNT_FILE,
    transactions,
    TRANSACTION_FILE,
    BASE_DIR,
    print_receipt,
)

    elif choice == "4":
         show_history(
                    transactions,
                    current_user,
                       )

    elif choice == "5":
         change_pin(
    accounts,
    current_user,
    ACCOUNT_FILE,
    transactions,
    TRANSACTION_FILE,
)

    elif choice == "6":
         transfer_money(
    accounts,
    current_user,
    ACCOUNT_FILE,
    transactions,
    TRANSACTION_FILE,
    BASE_DIR,
    print_receipt,
)

    elif choice == "7":
          print("\nThank You For Using Our ATM.")
          break

    else:
          print("\nInvalid Choice!")