from tkinter import *

class Input:
    def __init__(self, name, col_num, row_num):
        self.name = Label(text=name)
        self.input_place = Entry()
        self.name.grid(column=col_num, row=row_num)
        self.input_place.grid(column=col_num+1, row=row_num)

