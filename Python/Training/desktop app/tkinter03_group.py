# Import only those methods
# which are mentioned below, this way of
# importing methods is efficient
from tkinter import Tk, mainloop
from tkinter.ttk import Checkbutton, Button, LabelFrame

# Creating tkinter window with fixed geometry
root = Tk()
root.geometry('250x150')

# This will create a LabelFrame
label_frame = LabelFrame(root, text='This is Label Frame')
label_frame.pack(expand='yes', fill='both')

# Buttons
btn1 = Button(label_frame, text='Button 1')
btn1.place(x=30, y=10)
btn2 = Button(label_frame, text='Button 2')
btn2.place(x=130, y=10)

# Checkbuttons
chkbtn1 = Checkbutton(label_frame, text='Checkbutton 1')
chkbtn1.place(x=30, y=50)
chkbtn2 = Checkbutton(label_frame, text='Checkbutton 2')
chkbtn2.place(x=30, y=80)

# This creates infinite loop which generally
# waits for any interrupt (like keyboard or
# mouse) to terminate
mainloop()
