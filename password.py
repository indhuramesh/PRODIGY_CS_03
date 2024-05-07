def assess_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    special_chars = "!@#$%^&*()_-+=<>?/"
    if any(c in special_chars for c in password):
        score += 1

    return score

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)

    if strength <= 2:
        print("Weak password. The password must contain atleast a single uppercase letter and numeric alphabets and symbols")
    elif strength <= 4:
        print("Moderate password. It should be much stronger")
    elif strength >= 6:
        print("Strong password. Good job!")
    else:
        print("Very strong password. Well done!")

if __name__ == "__main__":
    main()
