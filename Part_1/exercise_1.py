# Add a label that says Welcome to My App! centered in the window.
# use tk.Label()

import tkinter as tk

root = tk.Tk()
root.title("Exercise 1")
root.geometry("300x300")

message = tk.Label(root, text="Welcome to My App!")
message.pack(pady=20)

root.mainloop()