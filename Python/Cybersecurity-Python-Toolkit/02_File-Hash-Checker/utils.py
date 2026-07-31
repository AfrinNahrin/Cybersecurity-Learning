import os


def print_banner():

    print("=" * 45)
    print("      FILE HASH CHECKER")
    print("         Version 2.0")
    print("=" * 45)


def check_file_exists(file_path):

    return os.path.isfile(file_path)
# -------------------------
# Display Main Menu
# -------------------------

def display_menu():

    print("\n========== MAIN MENU ==========")
    print("1. Generate File Hash")
    print("2. Verify SHA256 Hash")
    print("3. Exit")
    print("===============================")