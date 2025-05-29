from fitness_tracker.lib.models.user import User
from fitness_tracker.lib.models.workout import Workout
from fitness_tracker.lib.models.exercise import Exercise
from fitness_tracker.lib.models import session
from tabulate import tabulate

def create_user():
    name = input("Enter user's name: ").strip()
    if session.query(User).filter_by(name=name).first():
        print(f"User '{name}' already exists.")
        return
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    print(f"User '{name}' created!")

def list_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return
    print("\nUsers:")
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}")

def delete_user():
    list_users()
    try:
        user_id = int(input("Enter ID of user to delete: "))
    except ValueError:
        print("Invalid input.")
        return
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{user.name}' deleted.")
    else:
        print("User not found.")

def create_workout():
    list_users()
    try:
        user_id = int(input("Enter user ID to create workout for: "))
    except ValueError:
        print("Invalid input.")
        return
    user = session.query(User).get(user_id)
    if not user:
        print("User not found.")
        return
    new_workout = Workout(user=user)
    session.add(new_workout)
    session.commit()
    print(f"Workout created with ID {new_workout.id} for user '{user.name}'.")

def add_exercise():
    try:
        workout_id = int(input("Enter workout ID to add exercise to: "))
    except ValueError:
        print("Invalid input.")
        return
    workout = session.query(Workout).get(workout_id)
    if not workout:
        print("Workout not found.")
        return
    name = input("Enter exercise name (e.g., squats): ").strip()
    try:
        reps = int(input("Enter number of reps: "))
    except ValueError:
        print("Reps must be an integer.")
        return
    exercise = Exercise(name=name, reps=reps, workout=workout)
    session.add(exercise)
    session.commit()
    print(f"Added exercise '{name}' with {reps} reps to workout {workout.id}.")

def view_user_history():
    name = input("Enter user's name to view history: ").strip()
    user = session.query(User).filter_by(name=name).first()
    if not user:
        print(f"No user found with name '{name}'.")
        return
    rows = []
    for workout in user.workouts:
        if workout.exercises:
            for ex in workout.exercises:
                rows.append([workout.id, ex.name, ex.reps])
        else:
            rows.append([workout.id, "No exercises", "-"])
    if rows:
        print(f"\nFitness History for {user.name}:")
        print(tabulate(rows, headers=["Workout ID", "Exercise", "Reps"], tablefmt="grid"))
    else:
        print(f"No workouts found for {user.name}.")
