def register_user(users):
    print("=== Register User ===")
    username = input("Enter a new username: ").strip()
    if username in users:
        print("Username already exists. Please try a different one.")
        return
    password = input("Enter a new password: ").strip()
    users[username] = password
    print("Registration successful!")

def login_user(users):
    print("=== Login User ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    users = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")
