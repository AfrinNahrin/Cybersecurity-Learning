from utils import save_accounts, add_transaction


def login(accounts):

    attempts = 3

    while attempts > 0:

        account_number = input("\nEnter Account Number: ")
        pin = input("Enter ATM PIN: ")

        if account_number not in accounts:
            attempts -= 1
            print("Account Not Found!")
            print(f"Attempts Left: {attempts}")
            continue

        if accounts[account_number]["pin"] == pin:

            print("\n=========================")
            print("Login Successful!")
            print(f"Welcome {accounts[account_number]['name']}")
            print("=========================")

            return account_number

        attempts -= 1
        print(f"Wrong PIN! Attempts Left: {attempts}")

    print("\nAccount Locked!")
    return None


def check_balance(accounts, current_user):

    print("\n=========================")
    print("      ACCOUNT BALANCE")
    print("=========================")

    balance = accounts[current_user]["balance"]

    print(f"Account Holder : {accounts[current_user]['name']}")
    print(f"Balance        : {balance:.2f} TK")


def change_pin(accounts,
               current_user,
               account_file,
               transactions,
               transaction_file):

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

    save_accounts(account_file, accounts)

    add_transaction(
        accounts,
        transactions,
        transaction_file,
        current_user,
        "PIN Changed",
        0,
    )

    print("\nPIN Changed Successfully!")