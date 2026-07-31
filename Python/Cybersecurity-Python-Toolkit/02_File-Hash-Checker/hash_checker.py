# -------------------------
# Import Required Module
# -------------------------

import hashlib


# -------------------------
# Generate MD5 Hash
# -------------------------

def generate_md5(file_path):
    """
    Generate MD5 hash of a file.
    """

    try:

        # Open file in Binary Mode
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Generate MD5 Hash
        md5_hash = hashlib.md5(file_data).hexdigest()

        return md5_hash

    except FileNotFoundError:
        return "Error: File not found."

    except Exception as error:
        return f"Error: {error}"

# -------------------------
# Generate SHA256 Hash
# -------------------------

def generate_sha256(file_path):
    """
    Generate SHA256 hash of a file.
    """

    try:

        # Open file in Binary Mode
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Generate SHA256 Hash
        sha256_hash = hashlib.sha256(file_data).hexdigest()

        return sha256_hash

    except FileNotFoundError:
        return "Error: File not found."

    except Exception as error:
        return f"Error: {error}"
# -------------------------
# Verify Hash
# -------------------------

def verify_hash(generated_hash, user_hash):
    """
    Compare generated hash with user hash.
    """

    return generated_hash.lower() == user_hash.lower()