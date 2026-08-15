users={}
while True:
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        username=input("Enter username:")
        password=input("Enter passwoard: ")
        if username in users:
            print("username already exits!")
        else:
            users[username]=password
            print("Resistration successfull!")
    elif choice=="2":
        username=input('Enter username:')
        password=input("Enter password")
        if username in users and users[username]==password:
            print("Login sucessfully! Welcome",username)
        else:
            print("Invalid username or password!")
    elif choice=="3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
