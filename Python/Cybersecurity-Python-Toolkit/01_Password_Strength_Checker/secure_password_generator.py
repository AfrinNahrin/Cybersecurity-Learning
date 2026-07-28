import secrets
import string


def generate_secure_password(
    length,
    use_upper=True,
    use_lower=True,
    use_numbers=True,
    use_symbols=True
):

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()_+-="

    if not characters:
        return None

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password