import argparse

from app.database import Database
from app.models import Task

def add_task(title):
    db = Database()
    task = Task(title)
    db.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task.title, int(task.done))
    )
    print("Task added.")

def list_tasks():
    db = Database()
    cursor = db.execute("SELECT id, title, done FROM tasks")
    for row in cursor.fetchall():
        status = "✔" if row[2] else "❌"
        print(f"{row[0]} - {row[1]} [{status}]")

def complete_task(task_id):
    db = Database()
    db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    print("Task marked as completed.")

