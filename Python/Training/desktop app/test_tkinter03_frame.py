from tkinter import * 
root = Tk() 
root.geometry("300x150") 

w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 

frame = Frame(root) 
frame.pack() 

bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 

b1_button = Button(frame, text ="Geeks1", fg ="red") 
b1_button.pack( side = LEFT) 

b2_button = Button(frame, text ="Geeks2", fg ="brown") 
b2_button.pack( side = LEFT ) 

b3_button = Button(frame, text ="Geeks3", fg ="blue") 
b3_button.pack( side = LEFT ) 

b4_button = Button(bottomframe, text ="Geeks4", fg ="green") 
b4_button.pack( side = BOTTOM) 

b5_button = Button(bottomframe, text ="Geeks5", fg ="green") 
b5_button.pack( side = BOTTOM) 

b6_button = Button(bottomframe, text ="Geeks6", fg ="green") 
b6_button.pack( side = BOTTOM) 

root.mainloop() 
