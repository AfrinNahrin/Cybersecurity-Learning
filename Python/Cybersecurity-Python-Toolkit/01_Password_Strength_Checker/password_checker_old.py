import re
from common_passwords import COMMON_PASSWORDS
from patterns import SEQUENTIAL_PATTERNS
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
# Main Checker
# -------------------------

def check_password(password):

    score = 0
    feedback = []

    print("\n========== PASSWORD REPORT ==========\n")

    # Length
    if check_length(password):
        print("✅ Length Check              : Passed")
        score += 1
    else:
        print("❌ Length Check              : Failed")
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if check_uppercase(password):
        print("✅ Uppercase Check           : Passed")
        score += 1
    else:
        print("❌ Uppercase Check           : Failed")
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if check_lowercase(password):
        print("✅ Lowercase Check           : Passed")
        score += 1
    else:
        print("❌ Lowercase Check           : Failed")
        feedback.append("Add at least one lowercase letter.")

    # Number
    if check_number(password):
        print("✅ Number Check              : Passed")
        score += 1
    else:
        print("❌ Number Check              : Failed")
        feedback.append("Add at least one number.")

    # Special Character
    if check_special_character(password):
        print("✅ Special Character Check   : Passed")
        score += 1
    else:
        print("❌ Special Character Check   : Failed")
        feedback.append("Add at least one special character.")

    # Repeated Character Check
    if check_repeated_characters(password):
        print("⚠ Repeated Characters       : Found")
        feedback.append("Avoid repeated characters like aaa or 111.")
    else:
        print("✅ Repeated Characters       : Not Found")

       # Sequential Pattern Check
    if check_sequential_pattern(password):
        print("⚠ Sequential Pattern        : Found")
        feedback.append("Avoid sequential patterns like '1234', 'abcd', or 'qwerty'.")
    else:
        print("✅ Sequential Pattern        : Not Found")
        

    # Common Password Check
    if check_common_password(password):
        print("⚠ Common Password           : Yes")
        feedback.append("Avoid common passwords.")
    else:
        print("✅ Common Password           : No")

    print("\n==============================")
    print(f"Password Score : {score}/5")
    print(f"Strength       : {get_strength(score)}")

    print("\nSuggestions:")

    if not feedback:
        print("✅ Excellent! No suggestions.")
    else:
        for item in feedback:
            print(f"- {item}")