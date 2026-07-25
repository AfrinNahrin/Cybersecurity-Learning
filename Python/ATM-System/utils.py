import json
import uuid
import os
from datetime import datetime
# ==========================
# SAVE ACCOUNT DATA
# ==========================
def save_accounts(account_file, accounts):

    with open(account_file, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)

# ==========================
# SAVE TRANSACTION HISTORY
# ==========================
def save_transactions(transaction_file, transactions):

    with open(transaction_file, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)

# ==========================
# RECORD TRANSACTION
# ==========================
def add_transaction(accounts,
                    transactions,
                    transaction_file,
                    account_number,
                    transaction_type,
                    amount):

    transaction = {

        "transaction_id": str(uuid.uuid4())[:8],

        "date": datetime.now().strftime("%d-%m-%Y"),

        "time": datetime.now().strftime("%I:%M:%S %p"),

        "account": account_number,

        "type": transaction_type,

        "amount": amount,

        "balance": accounts[account_number]["balance"]

    }

    transactions.append(transaction)

    save_transactions(transaction_file, transactions)
    
# ==========================
# PRINT RECEIPT
# ==========================

def print_receipt(accounts,
                  account_number,
                  transaction_type,
                  amount,
                  base_dir):

    receipt = f"""
===================================
            ATM RECEIPT
===================================

Account Holder : {accounts[account_number]["name"]}
Account Number : {account_number}

Transaction    : {transaction_type}
Amount         : {amount:.2f} TK

Current Balance: {accounts[account_number]["balance"]:.2f} TK

Date           : {datetime.now().strftime("%d-%m-%Y")}
Time           : {datetime.now().strftime("%I:%M:%S %p")}

===================================
Thank You For Banking With Us
===================================
"""

    print(receipt)

    receipt_file = os.path.join(base_dir, "receipt.txt")

    with open(receipt_file, "w", encoding="utf-8") as file:
        file.write(receipt)