from utils import save_accounts, add_transaction
# ==========================
# DEPOSIT MONEY
# ==========================
def deposit(accounts,
            current_user,
            account_file,
            transactions,
            transaction_file,
            print_receipt):

    print("\n========== DEPOSIT ==========")

    try:
        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        accounts[current_user]["balance"] += amount

        save_accounts(account_file, accounts)

        add_transaction(
            accounts,
            transactions,
            transaction_file,
            current_user,
            "Deposit",
            amount,
        )

        print("\nDeposit Successful!")
        print(f"Current Balance: {accounts[current_user]['balance']:.2f} TK")

        print_receipt(current_user, "Deposit", amount)

    except ValueError:
        print("Please Enter Numbers Only!")
# ==========================
# WITHDRAW MONEY
# ==========================

def withdraw(accounts,
             current_user,
             account_file,
             transactions,
             transaction_file,
             print_receipt):

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

        save_accounts(account_file, accounts)

        add_transaction(
               accounts,
               transactions,
               transaction_file,
               current_user,
               "Withdraw",
                amount,
                   )

        print("\nWithdraw Successful!")
        print(f"Remaining Balance: {accounts[current_user]['balance']} TK")
        print_receipt(current_user, "Withdraw", amount)

    except ValueError:
        print("Please Enter Numbers Only!")
# ==========================
# TRANSACTION HISTORY
# ==========================

def show_history(transactions, current_user):

    print("\n========== TRANSACTION HISTORY ==========")

    found = False

    for transaction in transactions:

        if transaction["account"] == current_user:

            found = True

            print("--------------------------------")

            print("Transaction ID :", transaction["transaction_id"])

            print("Date           :", transaction["date"])

            print("Time           :", transaction["time"])

            print("Type           :", transaction["type"])

            print("Amount         :", transaction["amount"], "TK")

            print("Balance        :", transaction["balance"], "TK")

    if not found:

        print("No Transactions Found!")

# ==========================
# MONEY TRANSFER
# ==========================

def transfer_money(accounts,
                   current_user,
                   account_file,
                   transactions,
                   transaction_file,
                   print_receipt):

    receiver = input("\nEnter Receiver Account Number: ")

    if receiver not in accounts:
        print("Receiver Account Not Found!")
        return

    if receiver == current_user:
        print("You Cannot Transfer To Your Own Account!")
        return

    try:
        amount = float(input("Enter Transfer Amount: "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        if amount > accounts[current_user]["balance"]:
            print("Insufficient Balance!")
            return

        # Sender Balance
        accounts[current_user]["balance"] -= amount

        # Receiver Balance
        accounts[receiver]["balance"] += amount

        save_accounts(account_file, accounts)

        # Sender History
        add_transaction(
              accounts,
              transactions,
              transaction_file,
              current_user,
              "Transfer Sent",
              amount,
               )

        # Receiver History
        add_transaction(
            accounts,
            transactions,
            transaction_file,
            receiver,
            "Transfer Received",
            amount,
             )

        print("\nTransfer Successful!")
        print(f"{amount} TK Sent To {accounts[receiver]['name']}")
        print_receipt(current_user, "Transfer Sent", amount)

    except ValueError:
        print("Please Enter Numbers Only!")
