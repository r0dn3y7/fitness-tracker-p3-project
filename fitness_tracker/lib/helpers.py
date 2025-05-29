# lib/helpers.py

from lib.models import session
from lib.models.user import User
from lib.models.workout import Workout
from lib.models.exercise import Exercise

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
