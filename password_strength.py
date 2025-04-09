import re

def check_password_strength(password: str) -> str:
    """
    Check the strength of a password based on length and character variety.
    
    :param password: The password to check.
    :return: A string indicating the strength of the password.
    """
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "lowercase": re.search(r"[a-z]", password),
        "uppercase": re.search(r"[A-Z]", password),
        "digit": re.search(r"[0-9]", password),
        "special_char": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    }

    strength = sum(bool(val) for val in criteria.values())
    print("the strength in value", strength)  # Debugging line to check the strength value

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"
    
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")