correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password, remaining attempts: {remaining_attempts}.")
        if attempts == max_attempts:
            print("You've failed to enter the correct password more than 5 times.")