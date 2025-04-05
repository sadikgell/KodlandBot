import sqlite3

def show_tasks():
    output = ""
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            records = cursor.fetchall()
            for task_id, task, is_completed in records:
                checkbox = "[✔]" if is_completed else "[ ]"
                output += f"{checkbox} {str(task_id).rjust(3, '0')}: {task}\n"
            print(output)
            print("test show tasks successfully.")
    except Exception as error:
        print("Error while fetching tasks:", error)
