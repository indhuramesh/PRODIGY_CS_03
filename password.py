def assess_password_strength(password):
    score = 0

    # Length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    # Presence of uppercase letters
    if any(c.isupper() for c in password):
        score += 1

    # Presence of lowercase letters
    if any(c.islower() for c in password):
        score += 1

    # Presence of numbers
    if any(c.isdigit() for c in password):
        score += 1

    # Presence of special characters
    special_chars = "!@#$%^&*()_-+=<>?/"
    if any(c in special_chars for c in password):
        score += 1

    return score

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)

    if strength <= 2:
        print("Weak password. Consider making it longer and more complex.")
    elif strength <= 4:
        print("Moderate password. It could be stronger.")
    elif strength >= 6:
        print("Strong password. Good job!")
    else:
        print("Very strong password. Well done!")

if __name__ == "__main__":
    main()
