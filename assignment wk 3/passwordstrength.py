# Question 4 - Password Strength Checker

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special = "!@#$%^&*"

for password in passwords:

    print("\nPassword:", password)

    upper = False
    lower = False
    digit = False
    special_char = False

    for ch in password:

        if ch.isupper():
            upper = True

        if ch.islower():
            lower = True

        if ch.isdigit():
            digit = True

        if ch in special:
            special_char = True

    if len(password) < 8:
        print("Need at least 8 characters")

    if upper == False:
        print("Need uppercase letter")

    if lower == False:
        print("Need lowercase letter")

    if digit == False:
        print("Need a number")

    if special_char == False:
        print("Need special character")

    if len(password) >= 8 and upper and lower and digit and special_char:
        print("Strong password")

    else:
        print("Weak password")