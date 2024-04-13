# https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
from tkinter import *
from tkinter import messagebox 

root = Tk() 
root.geometry("300x200") 

w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 

messagebox.showinfo("showinfo", "Information") 
messagebox.showwarning("showwarning", "Warning") 
messagebox.showerror("showerror", "Error") 

root.mainloop() 
