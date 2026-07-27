import re
import math
import json
import os
import webbrowser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
HISTORY_FILE = os.path.join(REPORT_DIR, "password_history.txt")

from common_passwords import COMMON_PASSWORDS
from patterns import SEQUENTIAL_PATTERNS
from colorama import Fore, Style, init

init(autoreset=True)


# -------------------------
# Validation Functions
# -------------------------

def check_length(password):
    return len(password) >= 8


def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password))


def check_lowercase(password):
    return bool(re.search(r"[a-z]", password))


def check_number(password):
    return bool(re.search(r"\d", password))


def check_special_character(password):
    return bool(
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )


def check_repeated_characters(password):
    """
    Detects repeated characters like:
    aaa
    111
    $$$
    """
    return bool(re.search(r"(.)\1{2,}", password))


def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def check_sequential_pattern(password):
    password = password.lower()

    for pattern in SEQUENTIAL_PATTERNS:
        if pattern in password:
            return True

    return False

# -------------------------
# Password Strength
# -------------------------

def get_strength(score):

    if score == 5:
        return "Very Strong 💪"

    elif score == 4:
        return "Strong ✅"

    elif score == 3:
        return "Medium ⚠"

    else:
        return "Weak ❌"

# -------------------------
# Risk Level
# -------------------------

def get_risk_level(entropy):

    if entropy >= 60:
        return "Low 🟢"

    elif entropy >= 40:
        return "Medium 🟡"

    else:
        return "High 🔴"

# -------------------------
# Password Statistics
# -------------------------

def password_statistics(password):

    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    special = len(password) - upper - lower - digits

    return {
        "length": len(password),
        "uppercase": upper,
        "lowercase": lower,
        "numbers": digits,
        "special": special
    }

# -------------------------
# JSON Report Export
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(REPORT_DIR, exist_ok=True)

def save_report(password, score, entropy, risk_level, stats):
    os.makedirs("reports", exist_ok=True)

    report = {
        "password": password,
        "score": score,
        "entropy": entropy,
        "strength": get_strength(score),
        "risk_level": risk_level,
        "statistics": stats
    }

    file_path = os.path.join(
    REPORT_DIR,
    "password_report.json"
)
    

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("✅ JSON Report Saved Successfully!")
    print(f"📂 Saved to: {os.path.abspath(file_path)}")
    print(f"Saved JSON to: {file_path}")
    print(f"Current Working Directory: {os.getcwd()}")

# -------------------------
# Open Reports Automatically
# -------------------------

def open_reports():

    reports = [
        "reports/password_report.json",
        "reports/password_report.csv",
        "reports/password_report.txt"
    ]

    for report in reports:

        if os.path.exists(report):
            webbrowser.open(os.path.abspath(report))

# -------------------------
# Password History
# -------------------------

def save_password_history(password):

    os.makedirs(REPORT_DIR, exist_ok=True)

    with open(
        HISTORY_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(password + "\n")

def password_exists(password):

    if not os.path.exists(HISTORY_FILE):
        return False

    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        passwords = file.read().splitlines()

    return password in passwords

# -------------------------
# TXT Report Export
# -------------------------

def save_text_report(password, score, entropy, risk_level, stats, feedback):

    os.makedirs("reports", exist_ok=True)

    file_path = os.path.join(REPORT_DIR, "password_report.txt")

    with open(file_path, "w", encoding="utf-8") as file:

        file.write("========== PASSWORD REPORT ==========\n\n")

        file.write(f"Password   : {password}\n")
        file.write(f"Score      : {score}/5\n")
        file.write(f"Entropy    : {entropy} bits\n")
        file.write(f"Strength   : {get_strength(score)}\n")
        file.write(f"Risk Level : {risk_level}\n\n")

        file.write("----- Password Statistics -----\n")
        file.write(f"Length              : {stats['length']}\n")
        file.write(f"Uppercase Letters   : {stats['uppercase']}\n")
        file.write(f"Lowercase Letters   : {stats['lowercase']}\n")
        file.write(f"Numbers             : {stats['numbers']}\n")
        file.write(f"Special Characters  : {stats['special']}\n\n")

        file.write("Suggestions:\n")

        if not feedback:
            file.write("Excellent! No suggestions.\n")
        else:
            for item in feedback:
                file.write(f"- {item}\n")

    print("✅ TXT Report Saved Successfully!")

# -------------------------
# CSV Report Export
# -------------------------

def save_csv_report(password, score, entropy, risk_level, stats):

    os.makedirs("reports", exist_ok=True)

    file_path = os.path.join(REPORT_DIR, "password_report.csv")

    with open(file_path, "w", encoding="utf-8") as file:

        file.write(
            "Password,Score,Entropy,Strength,Risk Level,"
            "Length,Uppercase,Lowercase,Numbers,Special Characters\n"
        )

        file.write(
            f"{password},"
            f"{score},"
            f"{entropy},"
            f"{get_strength(score)},"
            f"{risk_level},"
            f"{stats['length']},"
            f"{stats['uppercase']},"
            f"{stats['lowercase']},"
            f"{stats['numbers']},"
            f"{stats['special']}"
        )

    print("✅ CSV Report Saved Successfully!")
# -------------------------
# Entropy Calculator
# -------------------------

def calculate_entropy(password):
    pool_size = 0

    if check_lowercase(password):
        pool_size += 26

    if check_uppercase(password):
        pool_size += 26

    if check_number(password):
        pool_size += 10

    if check_special_character(password):
        pool_size += 32

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)

    return round(entropy, 2)

# -------------------------
# Main Password Checker
# -------------------------

def check_password(password):

    score = 0
    feedback = []

    print(Fore.CYAN + "\n========== PASSWORD REPORT ==========\n")

    # Length Check
    if check_length(password):
        print(Fore.GREEN + "✅ Length Check              : Passed")
        score += 1
    else:
        print(Fore.RED + "❌ Length Check              : Failed")
        feedback.append("Password should be at least 8 characters.")

    # Uppercase Check
    if check_uppercase(password):
        print(Fore.GREEN + "✅ Uppercase Check           : Passed")
        score += 1
    else:
        print(Fore.RED + "❌ Uppercase Check           : Failed")
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Check
    if check_lowercase(password):
        print(Fore.GREEN + "✅ Lowercase Check           : Passed")
        score += 1
    else:
        print(Fore.RED + "❌ Lowercase Check           : Failed")
        feedback.append("Add at least one lowercase letter.")

    # Number Check
    if check_number(password):
        print(Fore.GREEN + "✅ Number Check              : Passed")
        score += 1
    else:
        print(Fore.RED + "❌ Number Check              : Failed")
        feedback.append("Add at least one number.")

    # Special Character Check
    if check_special_character(password):
        print(Fore.GREEN + "✅ Special Character Check   : Passed")
        score += 1
    else:
        print(Fore.RED + "❌ Special Character Check   : Failed")
        feedback.append("Add at least one special character.")

    # Repeated Character Check
    if check_repeated_characters(password):
        print(Fore.YELLOW + "⚠ Repeated Characters       : Found")
        feedback.append("Avoid repeated characters like 'aaa' or '111'.")
    else:
        print(Fore.GREEN + "✅ Repeated Characters       : Not Found")

    # Sequential Pattern Check
    if check_sequential_pattern(password):
        print(Fore.YELLOW + "⚠ Sequential Pattern        : Found")
        feedback.append("Avoid sequential patterns like '1234', 'abcd', or 'qwerty'.")
    else:
        print(Fore.GREEN + "✅ Sequential Pattern        : Not Found")

    # Common Password Check
    if check_common_password(password):
        print(Fore.YELLOW + "⚠ Common Password           : Yes")
        feedback.append("Avoid common passwords.")
    else:
        print(Fore.GREEN + "✅ Common Password           : No")
 # -------------------------
 # Password Report
 # -------------------------

    entropy = calculate_entropy(password)
    risk_level = get_risk_level(entropy)
    stats = password_statistics(password)
    save_report(
    password,
    score,
    entropy,
    risk_level,
    stats
          )
    save_text_report(
    password,
    score,
    entropy,
    risk_level,
    stats,
    feedback
         )
    save_csv_report(
    password,
    score,
    entropy,
    risk_level,
    stats
         )

    print(Fore.CYAN + "\n==============================")
    print(Fore.CYAN + f"Password Score : {score}/5")
    print(Fore.MAGENTA + f"Entropy        : {entropy} bits")
    print(Fore.GREEN + f"Strength       : {get_strength(score)}")
    print(Fore.YELLOW + f"Risk Level     : {risk_level}")

    print(Fore.CYAN + "\n----------- Password Statistics -----------")
    print(f"Length              : {stats['length']}")
    print(f"Uppercase Letters   : {stats['uppercase']}")
    print(f"Lowercase Letters   : {stats['lowercase']}")
    print(f"Numbers             : {stats['numbers']}")
    print(f"Special Characters  : {stats['special']}")

    print(Fore.CYAN + "\nSuggestions:")

    if not feedback:
        print("✅ Excellent! No suggestions.")
    else:
        for item in feedback:
            print(f"- {item}")
    open_reports()