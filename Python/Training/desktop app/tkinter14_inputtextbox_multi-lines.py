# https://www.geeksforgeeks.org/how-to-create-a-multiline-entry-with-tkinter/

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


root = tk.Tk()

root.title("ScrolledText Widget Example")

ttk.Label(root, text="ScrolledText Widget Example", font=("Times New Roman", 15)).grid(
    column=0, row=0
)
ttk.Label(root, text="Enter your comments :", font=("Bold", 12)).grid(column=0, row=1)

text_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=40, height=8, font=("Times New Roman", 15)
)

text_area.grid(column=0, row=2, pady=10, padx=10)

# placing cursor in text area
text_area.focus()
root.mainloop()
