import random
import tkinter as tk


pwd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]}@$#{()*:/,._-"

length = 32


def genpass():
    password = "".join(random.sample(pwd, length))
    label.config(text = password)
    window.clipboard_clear()
    window.clipboard_append(password)


window = tk.Tk()

label = tk.Label(text = "click to generate password", width = 36,height = 2)

button = tk.Button(
    text = "Generate",
    width = 15,
    height = 2,
    command = genpass
)

label.pack()
button.pack(pady = 5)

window.mainloop()