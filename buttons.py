from tkinter import *

class Buttons(Button):
    def __init__(self, name, col_num, row_num, width = 1,height = 1, func=None):
        super().__init__()
        self.button = Button(text=name, width=width, height=height, command=func)
        self.button.grid(column=col_num, row=row_num, padx=2, pady=2)


