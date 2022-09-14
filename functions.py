import random
import tkinter



def create_password():
    signs = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm', ',',
             '.', '/', '?', '>', '<', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^',
             '&', '*', '(', ')']
    password=""
    for _ in range(15):
        password += random.choice(signs)
    return password


def save(url, email, password):
    row = url + '\t' + email + '\t' + password + '\n'
    print(row)
    with open('passwords.txt','a') as file:
        file.write(row)






