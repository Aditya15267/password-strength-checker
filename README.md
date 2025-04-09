# Password Strength Checker

A simple command-line tool to evaluate the strength of a password based on common security criteria. Quick, offline, and beginner friendly.

## Features

- Checks password strength in real-time
- Evaluates
    - Minimum length (8+ characters)
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special Characters
- Return verdict: **Weak**, **Moderate**, or **Strong**
- Easy to customise for stricter policies

## How to use

1. Clone the repository:
    ```sh
    git clone https://github.com/Aditya15267/password-strength-checker.git
2. Run the script:
    ```sh
    python password_strength.py
    ```

## Example

```bash
Enter a password to check its strength: Pa$$word123
Password strength: Strong
```

Another one:

```bash
Enter a password to check its strength: hello123
Password strength: Weak
```