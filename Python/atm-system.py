# ==========================
# ATM MANAGEMENT SYSTEM V2
# ==========================

balance = 10000
correct_pin = "1234"
transaction_history = []


# ---------------------------
# Check Balance
# ---------------------------
def check_balance():
    print("\n========== BALANCE ==========")
    print(f"Current Balance: {balance} TK")


# ---------------------------
# Deposit
# ---------------------------
def deposit():
    global balance

    amount = float(input("Enter Deposit Amount: "))

    if amount <= 0:
        print("Invalid Amount!")

    else:
        balance += amount
        transaction_history.append(f"Deposited: {amount} TK")

        print("Deposit Successful!")
        print("Current Balance:", balance)


# ---------------------------
# Withdraw
# ---------------------------
def withdraw():
    global balance

    amount = float(input("Enter Withdraw Amount: "))

    if amount <= 0:
        print("Invalid Amount!")

    elif amount > balance:
        print("Insufficient Balance!")

    else:
        balance -= amount

        transaction_history.append(f"Withdraw: {amount} TK")

        print("Withdraw Successful!")
        print("Remaining Balance:", balance)


# ---------------------------
# Transaction History
# ---------------------------
def show_history():

    print("\n========== TRANSACTION HISTORY ==========")

    if len(transaction_history) == 0:
        print("No Transactions Yet!")

    else:
        for transaction in transaction_history:
            print(transaction)


# ---------------------------
# Change PIN
# ---------------------------
def change_pin():

    global correct_pin

    old_pin = input("Enter Current PIN: ")

    if old_pin == correct_pin:

        new_pin = input("Enter New PIN: ")
        confirm_pin = input("Confirm New PIN: ")

        if new_pin == correct_pin:
            print("New PIN cannot be the same as the old PIN!")

        elif new_pin == confirm_pin:

            if len(new_pin) == 4 and new_pin.isdigit():

                correct_pin = new_pin

                print("PIN Changed Successfully!")

            else:
                print("PIN Must Be Exactly 4 Digits!")

        else:
            print("PIN Does Not Match!")

    else:
        print("Incorrect Current PIN!")


# ==========================
# LOGIN
# ==========================

attempt = 3

while attempt > 0:

    pin = input("Enter ATM PIN: ")

    if pin == correct_pin:
        print("\nLogin Successful!")
        break

    else:
        attempt -= 1
        print("Wrong PIN!")
        print("Attempts Left:", attempt)

if attempt == 0:
    print("Account Locked!")
    exit()


# ==========================
# ATM MENU
# ==========================

while True:

    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        show_history()

    elif choice == "5":
        change_pin()

    elif choice == "6":
        print("\nThank You For Using Our ATM.")
        break

    else:
        print("Invalid Choice! Please Try Again.")