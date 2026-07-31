from hash_checker import generate_md5
from hash_checker import generate_sha256
from hash_checker import verify_hash

from utils import (
    print_banner,
    check_file_exists,
    display_menu
)


# -------------------------
# Main Program
# -------------------------

while True:

    print_banner()
    display_menu()

    choice = input("\nEnter Your Choice: ")

    # -------------------------
    # Option 1
    # -------------------------

    if choice == "1":

        file_path = input("\nEnter File Path: ")

        if not check_file_exists(file_path):

            print("\n❌ Error: File does not exist.")

        else:

            md5_hash = generate_md5(file_path)
            sha256_hash = generate_sha256(file_path)

            print("\n========== HASH RESULT ==========")

            print(f"\nMD5    : {md5_hash}")
            print(f"\nSHA256 : {sha256_hash}")

    # -------------------------
    # Option 2
    # -------------------------

    elif choice == "2":

        file_path = input("\nEnter File Path: ")

        if not check_file_exists(file_path):

            print("\n❌ Error: File does not exist.")

        else:

            sha256_hash = generate_sha256(file_path)

            user_hash = input("\nEnter SHA256 Hash: ")

            if verify_hash(sha256_hash, user_hash):

                print("\n✅ Hash Verified Successfully.")

            else:

                print("\n❌ Hash Does Not Match.")

    # -------------------------
    # Option 3
    # -------------------------

    elif choice == "3":

        print("\n👋 Thank you for using File Hash Checker.")
        break

    # -------------------------
    # Invalid Choice
    # -------------------------

    else:

        print("\n❌ Invalid Choice.")

    input("\nPress Enter to Continue...")