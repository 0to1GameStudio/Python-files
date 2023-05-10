import random
from tkinter import *
from tkinter import messagebox
text="abcdefghijklmnopqrstuvwxyz"
texts="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ntext="0231456789"
otext="9785634210"
ptext="0987653421"
ctext="9748210356"
rtext="ZYXWVUTSRQPONMLKJIHGFEDCBA"

window = Tk()
window.title("Captcha App")
window.geometry("165x110")
captcha = StringVar()
user_input = StringVar()

def set_captcha():
    #s=random.choice(text)
    #a=random.choice(texts)
    f=random.choice(ntext)
    d=random.choice(otext)
    q=random.choice(ptext)
    c=random.choice(ctext)
    #r=random.choice(rtext)
    cat = captcha.set(" ".join(f+d+q+c))
    if(user_input == cat or cat == e):
        sett=Label(window,text="Correct",font="Arial 11 normal")
        sett.pack()
        print("Correct")
        
    e.delete(0,END)           

sot = Label(window,textvariable = captcha,font = "Colonna-MT 16 normal")
sot.pack()
e = Entry(window,textvariable = user_input,font = "Arial 10 bold")
e.pack(ipady = 5)
Button(text = "Check",command = set_captcha ,font = "Arial 10").pack()

set_captcha()
window.mainloop()
