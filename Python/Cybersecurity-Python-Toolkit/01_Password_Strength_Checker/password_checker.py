import re
from common_passwords import COMMON_PASSWORDS


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
    Detects 3 or more consecutive repeated characters.
    Example: aaa, 111, $$$
    """
    return bool(re.search(r"(.)\1{2,}", password))


def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def get_strength(score):

    if score == 5:
        return "Very Strong 💪"

    elif score == 4:
        return "Strong ✅"

    elif score == 3:
        return "Medium ⚠"

    else:
        return "Weak ❌"


def check_password(password):

    score = 0
    feedback = []

    print("\n========== PASSWORD REPORT ==========\n")

    # Length
    if check_length(password):
        print("✅ Length Check            : Passed")
        score += 1
    else:
        print("❌ Length Check            : Failed")
        feedback.append("Password should be at least 8 characters.")

    # Uppercase
    if check_uppercase(password):
        print("✅ Uppercase Check         : Passed")
        score += 1
    else:
        print("❌ Uppercase Check         : Failed")
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if check_lowercase(password):
        print("✅ Lowercase Check         : Passed")
        score += 1
    else:
        print("❌ Lowercase Check         : Failed")
        feedback.append("Add at least one lowercase letter.")

    # Number
    if check_number(password):
        print("✅ Number Check            : Passed")
        score += 1
    else:
        print("❌ Number Check            : Failed")
        feedback.append("Add at least one number.")

    # Special Character
    if check_special_character(password):
        print("✅ Special Character Check : Passed")
        score += 1
    else:
        print("❌ Special Character Check : Failed")
        feedback.append("Add at least one special character.")

    # Common Password
    if check_common_password(password):
        print("⚠ Warning                 : Common Password")
        feedback.append("Avoid common passwords.")

    print("\n==============================")
    print(f"Password Score : {score}/5")
    print(f"Strength       : {get_strength(score)}")

    print("\nSuggestions:")

    if len(feedback) == 0:
        print("✅ No suggestions. Excellent password!")

    else:
        for item in feedback:
            print("-", item)