from fitness_tracker.lib.models.user import User
from fitness_tracker.lib.models.workout import Workout
from fitness_tracker.lib.models.exercise import Exercise
from fitness_tracker.lib.models import session  


def create_user():
    name = input("Enter the user's name: ")
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    print(f"User '{name}' created successfully!")

def list_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def delete_user():
    list_users()
    user_id = input("Enter the ID of the user to delete: ")
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("User not found.")
