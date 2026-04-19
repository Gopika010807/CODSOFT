import random
import string
import tkinter as tk
from tkinter import messagebox
import ctypes


try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter valid length")
        return

    chars = ""
    
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showerror("Error", "Select at least one option")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

    check_strength(password)

def check_strength(password):
    if len(password) < 8:
        strength_label.config(text="Strength: Weak", fg="#ff4d4d")
    elif len(password) < 12:
        strength_label.config(text="Strength: Medium", fg="#ffaa00")
    else:
        strength_label.config(text="Strength: Strong", fg="#00ffcc")

def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        copy_label.config(text="Copied!", fg="#00ffcc")
        root.after(1500, lambda: copy_label.config(text=""))

# ---------------- UI ----------------
root = tk.Tk()
root.title("G's Password Generator")
root.geometry("720x520")
root.configure(bg="#0a0f1c")
root.tk.call('tk', 'scaling', 1.2)

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT = ("Segoe UI", 12)
FONT_PASS = ("Consolas", 14, "bold")

# ----------- MAIN FRAME -----------
frame = tk.Frame(root, bg="#111827", highlightbackground="#00ffcc",
                 highlightthickness=2)
frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

# Branding Header
tk.Label(frame, text=" G's Password Generator ",
         font=FONT_TITLE, bg="#111827", fg="#00ffcc").pack(pady=15)

# Length
tk.Label(frame, text="Password Length",
         font=FONT, bg="#111827", fg="white").pack()

entry_length = tk.Entry(frame, font=("Segoe UI", 14), justify="center")
entry_length.pack(pady=8)

# Options
var_upper = tk.IntVar(value=1)
var_lower = tk.IntVar(value=1)
var_digits = tk.IntVar()
var_symbols = tk.IntVar()

tk.Checkbutton(frame, text="Uppercase (A-Z)", variable=var_upper,
               bg="#111827", fg="white", selectcolor="#1f2937",
               font=FONT).pack(anchor="w", padx=80)

tk.Checkbutton(frame, text="Lowercase (a-z)", variable=var_lower,
               bg="#111827", fg="white", selectcolor="#1f2937",
               font=FONT).pack(anchor="w", padx=80)

tk.Checkbutton(frame, text="Numbers (0-9)", variable=var_digits,
               bg="#111827", fg="white", selectcolor="#1f2937",
               font=FONT).pack(anchor="w", padx=80)

tk.Checkbutton(frame, text="Symbols (!@#)", variable=var_symbols,
               bg="#111827", fg="white", selectcolor="#1f2937",
               font=FONT).pack(anchor="w", padx=80)

# Generate Button
tk.Button(frame, text="Generate Password",
          font=FONT, bg="#00ffcc", fg="#000",
          padx=10, pady=6, relief="flat",
          command=generate_password).pack(pady=12)

# Password Display (Glowing Style)
result_var = tk.StringVar()
password_box = tk.Entry(frame, textvariable=result_var,
                        font=FONT_PASS, justify="center",
                        bd=0, bg="#020617", fg="#00ffcc",
                        insertbackground="#00ffcc")
password_box.pack(pady=10, ipady=6, ipadx=10)

# Fake glow border
glow_frame = tk.Frame(frame, bg="#00ffcc", height=2)
glow_frame.pack(fill="x", padx=60)

# Copy Button
tk.Button(frame, text="Copy Password",
          font=FONT, bg="#2563eb", fg="white",
          relief="flat", command=copy_password).pack(pady=6)

copy_label = tk.Label(frame, text="", font=FONT,
                      bg="#111827")
copy_label.pack()

# Strength Indicator
strength_label = tk.Label(frame, text="Strength: ",
                          font=FONT, bg="#111827",
                          fg="#00ffcc")
strength_label.pack(pady=10)

# Footer
tk.Label(root, text="Password Generator • Built by G",
         font=("Segoe UI", 10),
         bg="#0a0f1c", fg="gray").pack(side="bottom", pady=8)

root.mainloop()
