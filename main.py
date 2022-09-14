from tkinter import *
from inputs import Input
from buttons import Buttons

window = Tk()
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Input("Website", 0, 1)
email = Input("Email/Username", 0, 2)
password = Input("Password", 0, 3)
rand_password = Buttons("generate password", 2,3,15)
add_password = Buttons("Add",1,4,30)













window.mainloop()