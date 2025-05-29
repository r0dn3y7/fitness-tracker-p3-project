from fitness_tracker.lib.models.user import User
from fitness_tracker.lib.models import session

def create_user():
    name = input("Enter the user's name: ")
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    print(f"User '{name}' created successfully!")

def list_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}")

def delete_user():
    list_users()
    try:
        user_id = int(input("Enter the ID of the user to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("User not found.")
