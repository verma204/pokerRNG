import tkinter as tk
import random

root = tk.Tk()
root.title("RNG")
root.geometry("400x300")

result_label = tk.Label(
    root, text="Click anywhere on this window\nto generate a number!", font=("Arial", 14)
)
result_label.pack(expand=True)

def generate_number(event):
    num = random.randint(1, 100)
    result_label.config(text = f"Random Number: {num}")


seed_window = tk.Toplevel(root)
seed_window.title("Seed")

seed_window.grab_set()

seed_label = tk.Label(seed_window, text="Enter Seed: ")
seed_label.pack(pady=5)

entry_field = tk.Entry(seed_window, width=25)
entry_field.pack(pady=5)
entry_field.focus_set()

def submit_seed():
    user_seed = entry_field.get()
    random.seed(user_seed)

    root.bind("<Button-1>", generate_number)

    print(f"Seed captured: {user_seed}")
    seed_window.destroy()

submit_btn = tk.Button(seed_window, text="Submit", command=submit_seed)
submit_btn.pack(pady=5)

root.mainloop()
