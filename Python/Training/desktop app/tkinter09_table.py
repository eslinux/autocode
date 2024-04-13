# https://www.youtube.com/watch?v=i4qLI9lmkqw
# https://www.plus2net.com/python/tkinter-treeview.php




from tkinter import ttk
import tkinter as tk
# Creating tkinter my_w
my_w = tk.Tk()
my_w.geometry("260x280") 
my_w.title("www.plus2net.com")  
# Using treeview widget
trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=1,column=1,padx=30,pady=20)

# column identifiers 
trv["columns"] = ("1", "2")
# Defining headings, other option is tree
trv['show'] = 'tree' 
# width of columns and alignment 
trv.column("#0", width = 80, anchor ='c')
trv.column("1", width = 10, anchor ='c')
trv.column("2", width = 100, anchor ='c')
# Headings  
# respective columns
trv.heading("#0", text ="Label",anchor='c')
trv.heading("1", text ="id")
trv.heading("2", text ="Name",anchor='c')

trv.insert("",'end',iid=1,text='First',values=(1,'n1-Alex'))
trv.insert("",'end',iid=2,text='second',values=(2,'n2-Ravi'))
trv.insert("",'end',iid=3,text='third',values=(3,'n3-Ronn'))

my_w.mainloop()