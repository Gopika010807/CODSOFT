import tkinter as tk
from tkinter import messagebox
import json, os

TASKS_FILE = "tasks.json"

def load_tasks():
    return json.load(open(TASKS_FILE)) if os.path.exists(TASKS_FILE) else []

def save_tasks(tasks):
    json.dump(tasks, open(TASKS_FILE, "w"), indent=4)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def mark_done():
    sel = listbox.curselection()
    if sel:
        tasks[sel[0]]["done"] = True
        save_tasks(tasks)
        update_listbox()

def delete_task():
    sel = listbox.curselection()
    if sel:
        tasks.pop(sel[0])
        save_tasks(tasks)
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["done"]:
            display = f"✅ {task['task']}"   # green check for done
        else:
            display = f"☐ {task['task']}"   # empty box for pending
        listbox.insert(tk.END, display)

root = tk.Tk()
root.title("GoDo (Gopika’s To-Do)")
root.configure(bg="#D2B48C")  # warm tan background

tasks = load_tasks()

# Logo "G" at the top
logo_label = tk.Label(root, text="G", font=("Georgia", 36, "bold"), fg="#6B4226", bg="#D2B48C")
logo_label.pack(pady=5)

title_label = tk.Label(root, text="GoDo – Gopika’s To-Do", 
                       font=("Georgia", 18, "bold"), bg="#D2B48C", fg="#6B4226")
title_label.pack(pady=5)

frame = tk.Frame(root, bg="#D2B48C")
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10, font=("Georgia", 12), 
                     bg="#FFF8DC", fg="#3E2723", bd=3, relief="ridge", selectbackground="#B8860B")
listbox.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40, font=("Georgia", 12), bd=2, relief="groove", bg="#FFF8DC", fg="#3E2723")
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#D2B48C")
btn_frame.pack()

tk.Button(btn_frame, text="➕ Add Task", command=add_task, bg="#6B4226", fg="white", font=("Georgia", 11, "bold")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="✔ Mark Done", command=mark_done, bg="#6B4226", fg="white", font=("Georgia", 11, "bold")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="🗑 Delete Task", command=delete_task, bg="#6B4226", fg="white", font=("Georgia", 11, "bold")).grid(row=0, column=2, padx=5)

footer_label = tk.Label(root, text="☕ A goal without a plan is just a wish ☕", 
                        font=("Georgia", 12), bg="#D2B48C", fg="#3E2723")
footer_label.pack(pady=10)

update_listbox()
root.mainloop()
