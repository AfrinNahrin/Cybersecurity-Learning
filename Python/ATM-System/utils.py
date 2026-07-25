import json
import uuid
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