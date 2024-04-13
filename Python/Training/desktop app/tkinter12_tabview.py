# https://www.plus2net.com/python/tkinter-notebook.php
# https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/

import tkinter as tk
from tkinter import *
from tkinter import ttk

my_w = tk.Tk()
my_w.geometry("400x200")

my_tabs = ttk.Notebook(my_w)  # declaring

tab1 = ttk.Frame(my_tabs)
tab2 = ttk.Frame(my_tabs)

my_tabs.add(tab1, text="Tab-0")  # adding tab
my_tabs.add(tab2, text="Tab-1")  # adding tab
my_tabs.pack(expand=1, fill="both")

l1 = tk.Label(tab1, text="I am tab-0", bg="yellow", width=10)
l1.place(relx=0.4, rely=0.2)  # using place
b1 = tk.Button(tab1, text="I am tab 0")
b1.place(relx=0.4, rely=0.4)

l2 = tk.Label(tab2, text="I am tab-1", bg="yellow", width=10)
l2.grid(row=1, column=1)  # using grid
b2 = tk.Button(tab2, text="I am tab-1")
b2.grid(row=2, column=2)

my_w.mainloop()  # Keep the window open
