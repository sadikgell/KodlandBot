import sqlite3
import discord

TOKEN = "Your Token"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def add_task(task: str, is_completed: int = 0):
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task, is_completed) VALUES (?, ?)", (task, is_completed))
            conn.commit()
    except Exception as error:
        print("Error while adding task:", error)

def show_tasks() -> str:
    output = ""
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            records = cursor.fetchall()
            for task_id, task, is_completed in records:
                checkbox = "[✔]" if is_completed else "[ ]"
                output += f"{checkbox} {str(task_id).rjust(3, '0')}: {task}\n"
    except Exception as error:
        print("Error while fetching tasks:", error)
    return output

def delete_task(task_id: int):
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
    except Exception as error:
        print("Error while deleting task:", error)

def complete_task(task_id: int):
    try:
        with sqlite3.connect('Database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
            conn.commit()
    except Exception as error:
        print("Error while completing task:", error)

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
                print("Current tasks:\n", show_tasks())
                delete_task(1)
                print("Deleted task 1.")
    except Exception as error:
        print("Error during testing:", error)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content

    if content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif content.startswith('$add_task'):
        task = content[10:].strip()
        if task:
            add_task(task)
            await message.channel.send(f'Task `{task}` has been added!')
        else:
            await message.channel.send("Please provide a task description.")

    elif content.startswith('$show_tasks'):
        tasks = show_tasks()
        if tasks:
            await message.channel.send(f"```{tasks}```")
        else:
            await message.channel.send("No tasks found.")

    elif content.startswith('$delete_task'):
        try:
            task_id = int(content[13:].strip())
            delete_task(task_id)
            await message.channel.send(f'Task with ID `{task_id}` has been deleted!')
        except ValueError:
            await message.channel.send("Please enter a valid task ID.")

    elif content.startswith('$complete_task'):
        try:
            task_id = int(content[15:].strip())
            complete_task(task_id)
            await message.channel.send(f"Task with ID `{task_id}` marked as completed!")
        except ValueError:
            await message.channel.send("Please enter a valid task ID.")

    elif content.startswith('$test'):
        test_system()
        await message.channel.send("Test completed. Check the console for results.")

client.run(TOKEN)
