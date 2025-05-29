from fitness_tracker.lib.helpers import create_user, list_users, delete_user

def main():
    while True:
        print("\n==== Fitness Tracker Menu ====")
        print("1. Create User")
        print("2. List Users")
        print("3. Delete User")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            delete_user()
        elif choice == "0":
            print("Exiting... Stay strong 💪")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
