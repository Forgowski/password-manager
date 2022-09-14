from tkinter import *
from inputs import Input

window = Tk()
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
email = Input("email")












window.mainloop()