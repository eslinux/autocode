import tkinter as tk

from gui import CalculatorGUI


def main():
    root = tk.Tk()
    # make window resizable nicely
    root.geometry('370x450')
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
