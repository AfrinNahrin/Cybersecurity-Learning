from datetime import datetime
import os


# -------------------------
# Display Project Banner
# -------------------------

def print_banner():

    print("=" * 45)
    print("       PASSWORD GENERATOR")
    print("          Version 3.0")
    print("=" * 45)


# -------------------------
# Display Main Menu
# -------------------------

def display_menu():

    print("\n========== MAIN MENU ==========")
    print("1. Generate Password")
    print("2. Exit")
    print("===============================")


# -------------------------
# Save Passwords to File
# -------------------------

def save_passwords(password_list):

    # Current project folder
    current_dir = os.path.dirname(__file__)

    # Create generated_passwords folder if it doesn't exist
    folder_path = os.path.join(current_dir, "generated_passwords")
    os.makedirs(folder_path, exist_ok=True)

    # Password file path
    file_path = os.path.join(folder_path, "passwords.txt")

    # Save passwords
    with open(file_path, "a", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write(f"Generated : {datetime.now()}\n\n")

        for password, strength in password_list:

            file.write(f"Password : {password}\n")
            file.write(f"Strength : {strength}\n\n")

        file.write("=" * 50 + "\n\n")