import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in task_list.get(0, tk.END):
            file.write(task + "\n")

# Add a new task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showerror("Error", "Task cannot be empty!")

# Remove selected task
def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showerror("Error", "Please select a task to remove!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()

task_list = tk.Listbox(root, width=40, height=15)
task_list.pack(pady=10)

tk.Button(root, text="Remove Task", command=remove_task).pack()

# Load existing tasks
tasks = load_tasks()
for task in tasks:
    task_list.insert(tk.END, task)

root.mainloop()
