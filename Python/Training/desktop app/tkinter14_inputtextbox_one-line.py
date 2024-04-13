import tkinter
from tkinter import *
from tkinter import ttk


root = Tk()

L1 = ttk.Label(root, text="User Name")
L1.grid(row=0, column=0)
L2 = ttk.Label(root, text="Password")
L2.grid(row=1, column=0)

mystr = StringVar()
mystr.set("username@xyz.com")

entry = ttk.Entry(textvariable=mystr, state=DISABLED).grid(
    row=0, column=1, padx=10, pady=10
)

passwd = ttk.Entry().grid(row=1, column=1, padx=10, pady=10)
mainloop()
