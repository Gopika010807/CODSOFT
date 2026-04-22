import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("G's To-Do List")
        self.root.geometry("450x650")
        
        # Floral aesthetic colors
        self.bg_color = "#E2D6EE"  # Light lavender from the image
        self.list_bg = "#F4EFE6"   # Light cream/beige for the list area
        self.text_color = "#1A1A1A" # Dark text
        self.btn_bg = "#F2D5D9"    # Soft pink for buttons and entry
        
        self.root.configure(bg=self.bg_color)
        
        self.tasks = self.load_tasks()
        
        self.setup_ui()
        self.populate_list()
        
    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
        
    def save_tasks(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.tasks, f)
            
    def setup_ui(self):
        # --- Title ---
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(pady=(20, 10))
        
        # Using an elegant serif font to match the floral theme
        title_label = tk.Label(
            title_frame, 
            text="Daily\nto-do list", 
            font=("Georgia", 32, "bold"), 
            bg=self.bg_color, 
            fg=self.text_color
        )
        title_label.pack()
        
        # --- Main List Area ---
        self.list_frame = tk.Frame(self.root, bg=self.list_bg, bd=0, relief=tk.FLAT)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        # We add a slight border to mimic the rounded card
        self.list_frame_inner = tk.Frame(self.list_frame, bg=self.list_bg, bd=2, relief=tk.SOLID)
        self.list_frame_inner.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.listbox = tk.Listbox(
            self.list_frame_inner, 
            font=("Georgia", 14), 
            bg=self.list_bg, 
            fg=self.text_color, 
            selectbackground=self.bg_color, 
            selectforeground="black",
            activestyle="none",
            bd=0,
            highlightthickness=0
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        scrollbar = tk.Scrollbar(self.list_frame_inner)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        
        # --- Input Area ---
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(fill=tk.X, padx=30, pady=10)
        
        self.task_entry = tk.Entry(
            input_frame, 
            font=("Georgia", 14), 
            bg=self.btn_bg, 
            fg=self.text_color,
            relief=tk.FLAT,
            insertbackground=self.text_color
        )
        self.task_entry.pack(fill=tk.X, ipady=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        # --- Buttons Area ---
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(fill=tk.X, padx=30, pady=(0, 20))
        
        btn_style = {
            "font": ("Georgia", 12, "bold"),
            "bg": self.btn_bg,
            "fg": self.text_color,
            "activebackground": self.list_bg,
            "relief": tk.FLAT,
            "bd": 0,
            "cursor": "hand2",
            "pady": 8
        }
        
        add_btn = tk.Button(btn_frame, text="Add Task", command=self.add_task, **btn_style)
        add_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        
        done_btn = tk.Button(btn_frame, text="Toggle Done", command=self.mark_done, **btn_style)
        done_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        del_btn = tk.Button(btn_frame, text="Delete", command=self.delete_task, **btn_style)
        del_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        
    def populate_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            # Checkbox styles: [ ] for pending, [X] for done
            status = "☑" if task['done'] else "☐"
            display_text = f"{status} {task['text']}"
            self.listbox.insert(tk.END, display_text)
            
            # Gray out completed tasks
            if task['done']:
                self.listbox.itemconfig(tk.END, fg="#888888")
            
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "done": False})
            self.save_tasks()
            self.populate_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
            
    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"] # Toggle
            self.save_tasks()
            self.populate_list()
            self.listbox.selection_set(index) # Keep the item selected
        except IndexError:
            pass # Ignore if no item is selected
            
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.save_tasks()
            self.populate_list()
        except IndexError:
            pass # Ignore if no item is selected

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
