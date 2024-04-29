# import asyncio
# import tkinter as tk

# from async_tkinter_loop import async_handler, async_mainloop


# async def counter():
#     i = 0
#     while True:
#         i += 1
#         label.config(text=str(i))
#         await asyncio.sleep(1.0)


# root = tk.Tk()

# label = tk.Label(root)
# label.pack()

# tk.Button(root, text="Start", command=async_handler(counter)).pack()

# async_mainloop(root)


# https://pypi.org/project/async-tkinter-loop/
import tkinter as tk
from io import BytesIO

import httpx
from PIL import Image, ImageTk

from async_tkinter_loop import async_handler, async_mainloop


async def load_image(url):
    button.config(state=tk.DISABLED)
    label.config(text="Loading...", image="")

    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
        if response.status_code != 200:
            label.config(text=f"HTTP error {response.status_code}")
        else:
            content = response.content
            pil_image = Image.open(BytesIO(content))
            image = ImageTk.PhotoImage(pil_image)
            label.image = image
            label.config(image=image, text="")
            button.config(state=tk.NORMAL)


url = "https://picsum.photos/800/640"

root = tk.Tk()
root.geometry("800x640")

button = tk.Button(root, text="Load an image", command=async_handler(load_image, url))
button.pack()

label = tk.Label(root)
label.pack(expand=1, fill=tk.BOTH)

async_mainloop(root)


