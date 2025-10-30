import tkinter as tk

clicks = 0

root = tk.Tk()
root.title("Exercise 3")
root.geometry("500x400")

message = tk.Label(root, text="Press the button below")
message.pack(pady=30)


def on_button_click():
    root.configure(bg="lightblue")
    root.geometry("600x500")
    global clicks
    clicks += 1
    message.config(text=f"You pressed the button {clicks} times!", fg="blue", bg='black')

button = tk.Button(root, text="Press Me", command=on_button_click, bg="lime", fg="black")
button.pack(padx=40, pady=30)

message_reset = tk.Label(root, text="Press the button below to reset")
message_reset.pack(pady=10)

def reverse_effects():
    root.configure(bg="SystemButtonFace")
    root.geometry("500x400")
    global clicks
    clicks = 0
    message_reset.config(text="Press the button below to reset", fg="white", bg='SystemButtonFace')

button_reset = tk.Button(root, text="Reset", command=reverse_effects, bg="red", fg="white")
button_reset.pack(padx=40, pady=10)

root.mainloop()