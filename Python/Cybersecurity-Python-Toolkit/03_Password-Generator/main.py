from password_generator import generate_password
from password_generator import check_strength

from utils import print_banner
from utils import display_menu
from utils import save_passwords


# -------------------------
# Main Program
# -------------------------

while True:

    print_banner()
    display_menu()

    choice = input("\nEnter Your Choice: ")

    # -------------------------
    # Generate Password
    # -------------------------

    if choice == "1":

        symbol_choice = input(
            "\nInclude Special Characters? (y/n): "
        ).lower()

        use_symbols = symbol_choice == "y"

        try:

            length = int(input("\nEnter Password Length: "))

            if length < 8:

                print("\n❌ Password length must be at least 8.")

            else:

                total = int(input("\nHow many passwords do you want to generate? "))

                password_list = []

                print("\n========== GENERATED PASSWORDS ==========\n")

                for i in range(total):

                    password = generate_password(length, use_symbols)

                    strength = check_strength(password)

                    password_list.append((password, strength))

                    print(f"{i + 1}. {password}")
                    print(f"   Strength : {strength}\n")

                print("=========================================")

                # Save Passwords
                save_passwords(password_list)

                print("\n✅ Passwords saved successfully.")

        except ValueError:

            print("\n❌ Please enter a valid number.")

    # -------------------------
    # Exit
    # -------------------------

    elif choice == "2":

        print("\n👋 Thank you for using Password Generator.")
        break

    # -------------------------
    # Invalid Choice
    # -------------------------

    else:

        print("\n❌ Invalid Choice.")

    input("\nPress Enter to Continue...")