import re


def password_score(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimum 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    return score, feedback


password = input("Enter Password: ")

score, feedback = password_score(password)

print("\nPassword Score:", score, "/5")

if score == 5:
    print("Strength : Very Strong 💪")
elif score == 4:
    print("Strength : Strong ✅")
elif score == 3:
    print("Strength : Medium ⚠")
else:
    print("Strength : Weak ❌")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)