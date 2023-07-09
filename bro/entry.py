from tkinter import *

def submit():
    val = entry.get()
    print(val)
    submit_button.config(stae=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
     
window = Tk()

entry = Entry(window,
              font=("arial",50),
              show="*"#password   
              )
entry.insert(0,'spongebob')
entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command = submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command = delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command = backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()