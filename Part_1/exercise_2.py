import tkinter as tk

clicks = 0

def button_click():
    print("Button Clicked!")

    global clicks
    clicks += 1
    label.config(text=f"Button Clicked! {clicks} times")


root = tk.Tk()

root.title("Exercise 2")
root.geometry("400x300")


label = tk.Label(root, text="Click the button below!")
label.pack(pady=20)

button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop()