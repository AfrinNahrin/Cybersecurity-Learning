import random
import string


# -------------------------
# Password Generator
# -------------------------

def generate_password(
    length=12,
    uppercase=True,
    lowercase=True,
    numbers=True,
    symbols=True
):

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += "!@#$%^&*()_+-="

    if not characters:
        return None

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    return password