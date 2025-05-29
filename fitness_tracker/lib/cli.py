from fitness_tracker.lib.helpers import (
    create_user,
    list_users,
    delete_user,
    create_workout,
    add_exercise,
    view_user_history,
)
from fitness_tracker.lib.models import Base, engine

def main():
    Base.metadata.create_all(engine)  # Make sure tables exist

    while True:
        print("\n==== Fitness Tracker Menu ====")
        print("1. Create User")
        print("2. List Users")
        print("3. Delete User")
        print("4. Create Workout")
        print("5. Add Exercise to Workout")
        print("6. View User Fitness History")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            create_workout()
        elif choice == "5":
            add_exercise()
        elif choice == "6":
            view_user_history()
        elif choice == "0":
            print("Goodbye! Stay strong 💪")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
