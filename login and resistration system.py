
users = {}

while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")

        if username == "":
            print("Username cannot be empty!")

        elif username in users:
            print("Username already exists!")

        else:
            password = input("Enter password: ")

            if len(password) < 6:
                print("Password must contain at least 6 characters!")

            else:
                confirm_password = input("Confirm password: ")

                if password == confirm_password:
                    users[username] = password
                    print("Registration successful!")

                else:
                    print("Passwords do not match!")

    elif choice == "2":
        username = input("Enter username: ")

        if username not in users:
            print("Username not found!")

        else:
            attempts = 3

            while attempts > 0:
                password = input("Enter password: ")

                if users[username] == password:
                    print("Login successful! Welcome", username)
                    break

                else:
                    attempts -= 1
                    print("Incorrect password!")
                    print("Attempts remaining:", attempts)

            if attempts == 0:
                print("Too many incorrect attempts!")

    elif choice == "3":
        print("Thank you for using Login System!")
        break

    else:
        print("Invalid choice! Please try again.")
