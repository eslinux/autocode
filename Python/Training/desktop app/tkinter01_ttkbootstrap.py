# https://ttkbootstrap.readthedocs.io/en/version-0.5/overview.html#why-does-this-project-exist

from ttkbootstrap import Style
from tkinter import ttk

style = Style()

window = style.master

ttk.Button(window, text="Submit", style='success.TButton').pack(side='left', padx=5, pady=10)
ttk.Button(window, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)
ttk.Checkbutton(window, text='include', style='Roundtoggle.Toolbutton').pack(side='left', padx=5, pady=10)
window.mainloop()




