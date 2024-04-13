import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# create the root window
root = tk.Tk()
root.title("Tkinter Yes/No Dialog")
root.geometry("300x150")


# click event handler
def confirm():
    answer = messagebox.askyesno(
        title="confirmation", message="Are you sure that you want to quit?"
    )
    if answer:
        print("click YES")
    else:
        print("click NO")

ttk.Button(root, text="Ask Yes/No", command=confirm).pack(expand=True)


# start the app
root.mainloop()


# The same with:
# messagebox.askquestion("askquestion", "Are you sure?") 
# messagebox.askokcancel("askokcancel", "Want to continue?") 
# messagebox.askyesno("askyesno", "Find the value?") 
# messagebox.askretrycancel("askretrycancel", "Try again?") 
