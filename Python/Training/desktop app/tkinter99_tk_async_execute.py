# https://tkinter-async-execute.readthedocs.io/en/v1.2.x/

from tkinter import ttk
import tkinter as tk
import asyncio

import tk_async_execute as tae  # pip install tkinter-async-execute


async def async_function():
    # Call tkinter widget methods.
    print("Disabling button")
    tae.tk_execute(bnt.config, text="Running...")
    tae.tk_execute(bnt.config, state="disabled")  # Thread safe exection
    await asyncio.sleep(5)
    print("Enabling button")
    tae.tk_execute(bnt.config, text="Click me")
    tae.tk_execute(bnt.config, state="normal")
    

def button_clicked():
    # Call async function
    # visible=True if you want to display progress bar
    tae.async_execute(
        async_function(),
        wait=True,
        visible=False,
        pop_up=True,
        callback=None,
        master=root,
    )


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x200")
    bnt = ttk.Button(root, text="Click me", command=button_clicked, width=20)
    bnt.pack()

    tae.start()  # Starts the asyncio event loop in a different thread.
    root.mainloop()  # Main Tkinter loop
    tae.stop()  # Stops the event loop and closes it.
