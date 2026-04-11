from tkinter import *
from tkinter import ttk
from logic import evaluate_expression
import base64
import io
from PIL import Image, ImageTk
import threading


class CalculatorGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent = parent
        self.parent.title("Calculator")
        self.grid(sticky=(N, S, E, W))

        # load icon from base64 resource
        self._load_icon()

        self.entry_var = StringVar()
        self._create_widgets()

        # keybindings
        self.parent.bind('<Return>', lambda e: self._calculate())
        self.parent.bind('<BackSpace>', lambda e: self._backspace())

    def _load_icon(self):
        try:
            from resources import icon_png_data
            icon_png = icon_png_data.icon_png
        except Exception:
            icon_png = None

        if icon_png:
            data = base64.b64decode(icon_png)
            image = Image.open(io.BytesIO(data))
            self.icon = ImageTk.PhotoImage(image)
            try:
                self.parent.iconphoto(False, self.icon)
            except Exception:
                pass

    def _create_widgets(self):
        entry = ttk.Entry(self, textvariable=self.entry_var, font=('Segoe UI', 16))
        entry.grid(row=0, column=0, columnspan=4, sticky=(W, E), pady=(0, 10))

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, r, c) in buttons:
            btn = ttk.Button(self, text=text, command=(lambda t=text: self._on_button(t)))
            btn.grid(row=r, column=c, sticky=(W, E), padx=4, pady=4)

        # extra controls
        clear = ttk.Button(self, text='C', command=self._clear)
        clear.grid(row=5, column=0, sticky=(W, E), padx=4, pady=4)
        back = ttk.Button(self, text='⌫', command=self._backspace)
        back.grid(row=5, column=1, sticky=(W, E), padx=4, pady=4)
        func = ttk.Button(self, text='sin', command=lambda: self._insert('sin('))
        func.grid(row=5, column=2, sticky=(W, E), padx=4, pady=4)
        pi = ttk.Button(self, text='pi', command=lambda: self._insert('pi'))
        pi.grid(row=5, column=3, sticky=(W, E), padx=4, pady=4)

        for i in range(4):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)

    def _on_button(self, text):
        if text == '=':
            self._calculate()
            return
        self._insert(text)

    def _insert(self, text):
        self.entry_var.set(self.entry_var.get() + text)

    def _clear(self):
        self.entry_var.set('')

    def _backspace(self):
        self.entry_var.set(self.entry_var.get()[:-1])

    def _calculate(self):
        expr = self.entry_var.get()
        # Disable the entry to prevent multiple calculations
        self.entry_var.set("Calculating...")
        # Run calculation in a separate thread
        threading.Thread(target=self._calculate_async, args=(expr,), daemon=True).start()

    def _calculate_async(self, expr):
        try:
            result = evaluate_expression(expr)
            # Update UI from main thread
            self.parent.after(0, lambda: self.entry_var.set(str(result)))
        except Exception as e:
            # Update UI from main thread
            self.parent.after(0, lambda: self.entry_var.set('Error'))
