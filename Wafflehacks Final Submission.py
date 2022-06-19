#Team Realscape by Dev Chitale
#Wafflehacks Final Submission
#Categories entered in: Best Beginner Hack, Best Student Food Insecurity Hack,
#Best Art and Music Hack, Best Healthcare Hack, Best Connections Hack

import tkinter as tk
from tkinter import messagebox
import random

window= tk.Tk()

frame = tk.Canvas(window, width = 300, height = 300)
frame.pack()

a = str("Did you have a good meal today?")
b = str("Did you drink water today?")

c = str("That new drake album was the greatest album of all time.")
d = str("Lofi beats are boring.")

e = str("You should go on a run today, make it a half marathon while you're at it?")
f = str("Taking breaks are for quitters.")

g = str("You should send a message in the family groupchat.")
h = str("Reach out to people on LinkedIn.")

list = [a,b,c,d,e,f,g,h]

def prompt():
    MsgBox = tk.messagebox.askquestion ('Warning!',"Press 'no' to continue...",icon = 'warning')
    while MsgBox == "no":
        MsgBox = tk.messagebox.askquestion ('Warning!',(random.choice(list)),icon = 'warning')

button001 = tk.Button (window, text='Click for a reality check!',command=prompt,bg='blue',fg='white')
frame.create_window(150, 150, window=button001)

window.mainloop()