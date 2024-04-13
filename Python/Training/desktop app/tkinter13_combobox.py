# https://www.plus2net.com/python/tkinter-Combobox.php


import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
def my_upd(*args):
    l1.config(text=sel.get() + ' : '+ str(cb1.current()))
def my_insert(): # adding data to Combobox
    #if e1.get() not in cb1['values']:
    cb1['values'] +=(e1.get(),) # add option
sel=tk.StringVar() # string variable 
months=['Jan','Feb','Mar','Apr','May','Jun']
cb1 = ttk.Combobox(my_w, values=months,width=7,textvariable=sel)
cb1.grid(row=1,column=1,padx=10,pady=20)

l1=tk.Label(my_w,text='Month')
l1.grid(row=1,column=2)

e1=tk.Entry(my_w,bg='Yellow',width=10)
e1.grid(row=1,column=3)

b1=tk.Button(my_w,text='Add',command=lambda: my_insert())
b1.grid(row=1,column=4)

sel.trace_add('write',my_upd)
my_w.mainloop()  # Keep the window open