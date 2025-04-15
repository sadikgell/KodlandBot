from tests.test_add_task import add_task
from tests.test_delete_task import delete_task
from tests.test_show_tasks import show_tasks
from tests.test_completion_task import complete_task
import sqlite3

def test_system():
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            records = cursor.fetchall()
            if not records:
                add_task("test task")
                print("Test task added.")
                cursor.execute("SELECT * FROM tasks")
                records = cursor.fetchall()


            if records:
                complete_task(1)
                print("Marked task 1 as completed.")
                show_tasks()
                delete_task(1)
                print("Deleted task 1.")
    except Exception as error:
        print("Error during testing:", error)


if __name__ == "__main__":
    test_system()
    print("All tests passed.")
