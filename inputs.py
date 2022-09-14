from tkinter import *

class Input:
    def __init__(self, name, col_num, row_num):
        self.name = Label(text=name, height=2)
        self.input_place = Entry()
        self.name.grid(column=col_num, row=row_num, pady=2, padx=2)
        self.input_place.grid(column=col_num+1, row=row_num, pady=2, padx=2)

