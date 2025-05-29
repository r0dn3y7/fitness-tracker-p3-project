# 🏋️ Fitness Tracker CLI App

Welcome to the Fitness Tracker! This is a command-line Python application that helps users track their workouts and exercises, all stored using a SQLite database through SQLAlchemy ORM.

Perfect for anyone who lifts weights, runs marathons, or just loves typing into terminals.

---

## 📌 Features

- 🧍 Create, list, and delete users
- 🏋️ Create workouts for each user
- 💪 Add exercises to workouts (e.g., squats, push-ups)
- 🔍 View a user's full fitness history
- 🗃 All data stored persistently in `fitness.db`

---

## 🛠️ Tech Stack

- Python 3
- SQLAlchemy (ORM)
- SQLite (for local storage)
- Pipenv (for virtual environment)

---

## 🗂️ Project Structure

```bash
fitness_tracker/
├── Pipfile               
├── README.md             
└── lib/
    ├── models/           
    │   ├── __init__.py   
    │   ├── user.py       
    │   ├── workout.py    
    │   └── exercise.py  
    ├── cli.py            
    ├── helpers.py        
    └── debug.py          
