import sqlite3

def delete_task(task_id: int):
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            print("test task deleted successfully.")
    except Exception as error:
        print("Error while deleting task:", error)
