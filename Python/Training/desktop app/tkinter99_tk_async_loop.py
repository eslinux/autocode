import asyncio
from async_tkinter_loop import async_handler, async_mainloop
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from threading import Lock

async def btn_cancel():
    global g_isCancel
    g_isCancel = True
    print("btn_cancel: ", g_isCancel)

async def btn_click():
    global g_isCancel
    g_isCancel = False
    print("button clicked !")
    b1.config(state="disable", text="Running ...")
    while not g_isCancel:
        print("btn_click: ", g_isCancel)
        await asyncio.sleep(1.0)

    b1.config(state="normal", text="run")

if __name__ == "__main__":
    lock = Lock()
    g_isCancel = False

    # new approach
    root = ttk.Window(size=(720, 150))
    # root.geometry("720x150") #or use this api

    b1 = ttk.Button(root, text='run', bootstyle=PRIMARY, command=async_handler(btn_click))
    b1.pack(padx=5, pady=5)
    b2 = ttk.Button(root, text='cancel', bootstyle=SECONDARY, command=async_handler(btn_cancel))
    b2.pack(padx=5, pady=5)

    async_mainloop(root)
    





# # https://pypi.org/project/async-tkinter-loop/
# import tkinter as tk
# from io import BytesIO

# import httpx
# from PIL import Image, ImageTk

# from async_tkinter_loop import async_handler, async_mainloop


# async def load_image(url):
#     button.config(state=tk.DISABLED)
#     label.config(text="Loading...", image="")

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, follow_redirects=True)
#         if response.status_code != 200:
#             label.config(text=f"HTTP error {response.status_code}")
#         else:
#             content = response.content
#             pil_image = Image.open(BytesIO(content))
#             image = ImageTk.PhotoImage(pil_image)
#             label.image = image
#             label.config(image=image, text="")
#             button.config(state=tk.NORMAL)


# url = "https://picsum.photos/800/640"

# root = tk.Tk()
# root.geometry("800x640")

# button = tk.Button(root, text="Load an image", command=async_handler(load_image, url))
# button.pack()

# label = tk.Label(root)
# label.pack(expand=1, fill=tk.BOTH)

# async_mainloop(root)


