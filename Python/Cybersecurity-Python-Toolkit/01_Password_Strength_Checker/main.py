from password_checker import check_password


def show_menu():

    print("=" * 40)
    print("   Cybersecurity Password Toolkit")
    print("=" * 40)
    print("1. Check Password")
    print("2. Exit")
    print("=" * 40)


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("\nEnter Password: ")
        check_password(password)

        input("\nPress Enter to continue...")

    elif choice == "2":

        print("\nThank you for using Password Toolkit.")
        break

    else:

        print("\nInvalid Choice!")