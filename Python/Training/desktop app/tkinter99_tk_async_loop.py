import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
import threading

def btn_click():
    print("button clicked !")
    lb.config(text="-:-")
    threading.Thread(target=background_thread).start()

def background_thread():
    print("start...")
    for counter in range(0, 10):
        time.sleep(1)
        root.event_generate("<<event1>>", when="tail", state=counter)
    print("end...")

def event_handler(evt):  # runs in main thread
    print(evt.state)  #data from event
    lb.config(text=f"{evt.state}") #update UI here

if __name__ == "__main__":
    root = ttk.Window(size=(720, 150))

    b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY, command=btn_click)
    b1.pack(side=LEFT, padx=5, pady=5)

    lb = ttk.Label(root, text="hihi")
    lb.pack(side=LEFT, padx=5, pady=5)

    root.bind("<<event1>>", event_handler)  # event triggered by background thread
    root.mainloop()

