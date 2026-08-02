import random
import string


# -------------------------
# Generate Password
# -------------------------

def generate_password(length, use_symbols):
    """
    Generate a random password.
    """

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits
    )

    # Add Special Characters
    if use_symbols:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


# -------------------------
# Check Password Strength
# -------------------------

def check_strength(password):
    """
    Check password strength.
    """

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "🔴 Weak"

    elif score <= 4:
        return "🟡 Medium"

    else:
        return "🟢 Strong"