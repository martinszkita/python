from tkinter import *
from PIL import ImageTk, Image



def click():
    global count
    count +=1
    print("you clicked the button " + str(count)+" times!")

count = 0

window = Tk()

photo = ImageTk.PhotoImage(Image.open("bro/like.png"))#use relative path
button = Button(window,
                text="click me !",
                command=click,#callback, so no "()"
                font = ("comic sans",30),
                fg='#00ff00',
                bg='#000000',
                activeforeground='#00ff00',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='bottom'
                )

button.pack()









window.mainloop()