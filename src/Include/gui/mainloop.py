# this will be the main event loop of the gui

from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("600x750")
root.title("WxCLI")
window = ttk.Frame(root, padding=10)
window.grid(column=3, row=3)
ttk.Label(window, text="Current warnings for your area").grid(column=2, row=1)

root.mainloop()