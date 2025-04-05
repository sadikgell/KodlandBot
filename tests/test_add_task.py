import sqlite3

def add_task(task: str, is_completed: int = 0):
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task, is_completed) VALUES (?, ?)", (task, is_completed))
            conn.commit()
            print("test task added successfully.")
    except Exception as error:
        print("Error while adding task:", error)