import sqlite3

def complete_task(task_id: int):
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
            conn.commit()
            print("test completion task successfully.")
    except Exception as error:
        print("Error while completing task:", error)