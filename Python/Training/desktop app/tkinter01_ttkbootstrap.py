# https://pypi.org/project/ttkbootstrap/
# https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def btn_click():
    print("button clicked !")

if __name__ == "__main__":
    # new approach
    root = ttk.Window(size=(720, 150))
    # root.geometry("720x150") #or use this api

    b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY, command=btn_click)
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = ttk.Button(root, text='secondary', bootstyle=SECONDARY)
    b2.pack(side=LEFT, padx=5, pady=5)

    b3 = ttk.Button(root, text='success', bootstyle=SUCCESS)
    b3.pack(side=LEFT, padx=5, pady=5)

    b4 = ttk.Button(root, text='info', bootstyle=INFO)
    b4.pack(side=LEFT, padx=5, pady=5)

    b5 = ttk.Button(root, text='warning', bootstyle=WARNING)
    b5.pack(side=LEFT, padx=5, pady=5)

    b6 = ttk.Button(root, text='danger', bootstyle=DANGER)
    b6.pack(side=LEFT, padx=5, pady=5)

    b7 = ttk.Button(root, text='light', bootstyle=LIGHT)
    b7.pack(side=LEFT, padx=5, pady=5)

    b8 = ttk.Button(root, text='dark', bootstyle=DARK)
    b8.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()







# # https://ttkbootstrap.readthedocs.io/en/latest/gallery/textreader/

# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from tkinter.filedialog import askopenfilename
# from tkinter.scrolledtext import ScrolledText


# class TextReader(ttk.Frame):

#     def __init__(self, master):
#         super().__init__(master, padding=15)
#         self.filename = ttk.StringVar()
#         self.pack(fill=BOTH, expand=YES)
#         self.create_widget_elements()

#     def create_widget_elements(self):
#         """Create and add the widget elements"""
#         style = ttk.Style()
#         self.textbox = ScrolledText(
#             master=self,
#             highlightcolor=style.colors.primary,
#             highlightbackground=style.colors.border,
#             highlightthickness=1,
#         )
#         self.textbox.pack(fill=BOTH)
#         default_txt = "Click the browse button to open a new text file."
#         self.textbox.insert(END, default_txt)

#         file_entry = ttk.Entry(self, textvariable=self.filename)
#         file_entry.pack(side=LEFT, fill=X, expand=YES, padx=(0, 5), pady=10)

#         browse_btn = ttk.Button(self, text="Browse", command=self.open_file)
#         browse_btn.pack(side=RIGHT, fill=X, padx=(5, 0), pady=10)

#     def open_file(self):
#         path = askopenfilename()
#         if not path:
#             return

#         with open(path, encoding="utf-8") as f:
#             self.textbox.delete("1.0", END)
#             self.textbox.insert(END, f.read())
#             self.filename.set(path)


# if __name__ == "__main__":

#     app = ttk.Window("Text Reader", "sandstone")
#     TextReader(app)
#     app.mainloop()




