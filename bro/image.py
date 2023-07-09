from tkinter import *
from PIL import ImageTk, Image

window = Tk()

geo_str = "420x420"
window.geometry(geo_str)  # takes string
window.title("my cool window")

photo = ImageTk.PhotoImage(Image.open("bro/images.png"))
window.config(bg="blue")
label = Label(
    window, 
    text="hello world", 
    font=("arial", 40, "bold"), 
    fg="yellow", 
    bg="black",
    relief=RAISED,
    bd = 10,
    padx=50,
    pady=50,
    image=photo,
    compound='bottom'
)
label.pack()
# label.place(x=110,y=110)

window.mainloop()  # places window , listens for events
