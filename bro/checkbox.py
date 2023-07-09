from tkinter import *


def display():
    if(x.get() ==1):
        print("agree")
    else:
        print("dont agree")
window = Tk()

x = IntVar()
check_button=Checkbutton(window,
                         text="I agree to something",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         fg='#00ff00',
                         activebackground='black',
                         activeforeground="#00ff00"
                         )
check_button.pack()


window.mainloop()