from password_generator import generate_password
from secure_password_generator import generate_secure_password
from password_checker import (
    check_password,
    view_password_history,
    clear_password_history
)
def show_menu():

    print("=" * 45)
    print("     Cybersecurity Password Toolkit")
    print("=" * 45)
    print("1. Check Password")
    print("2. View Password History")
    print("3. Clear Password History")
    print("4. Generate Secure Password")
    print("5. Exit")
    print("=" * 45)
while True:

    show_menu()

    choice = input("Enter your choice: ")


    if choice == "1":

        password = input("\nEnter Password: ")

        check_password(password)

        input("\nPress Enter to continue...")


    elif choice == "2":

        view_password_history()

        input("\nPress Enter to continue...")


    elif choice == "3":

        clear_password_history()

        input("\nPress Enter to continue...")


    elif choice == "4":

        length = int(input("\nPassword Length: "))

        upper = input("Include Uppercase? (y/n): ").lower() == "y"
        lower = input("Include Lowercase? (y/n): ").lower() == "y"
        numbers = input("Include Numbers? (y/n): ").lower() == "y"
        symbols = input("Include Symbols? (y/n): ").lower() == "y"


        password = generate_secure_password(
            length,
            upper,
            lower,
            numbers,
            symbols
        )


        if password is None:

            print("\n❌ Please select at least one character type.")


        else:

            print("\nGenerated Secure Password:\n")
            print(password)

            print("\nChecking Generated Password...\n")

            check_password(password)


        input("\nPress Enter to continue...")


    elif choice == "5":

        print("\nThank you for using Password Toolkit.")

        break


    else:

        print("\n❌ Invalid Choice!")