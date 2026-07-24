import json
import os

BASE_DIR = os.path.dirname(__file__)

ACCOUNT_FILE = os.path.join(BASE_DIR, "account.json")
TRANSACTION_FILE = os.path.join(BASE_DIR, "transaction_log.json")

print("========== ATM SYSTEM V3 ==========")

with open(ACCOUNT_FILE, "r", encoding="utf-8") as file:
    accounts = json.load(file)

with open(TRANSACTION_FILE, "r", encoding="utf-8") as file:
    transactions = json.load(file)

print("Accounts Loaded Successfully!")
print(accounts)

print("Transactions Loaded Successfully!")
print(transactions)