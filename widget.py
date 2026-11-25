from tkinter import *
from datetime import date
root = Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')


lb1 = Label(root,text = 'Hello  World' , fg = "white" , bg = "blue" , height = 1 , width = 300)
name_lb1 = Label (root,text = 'Name' , fg = "white" , bg = "black" , height = 1 , width = 300)
name_entry = Entry()
def display():
    name = name_entry.get()
    global message 
    message = "Welcome to the application \n  Today's date is :" 
    greet = "Hello " +name + "\n"
    text_box.insert (END, greet)
    text_box.insert (END, message)
    text_box.insert (END, date.today())
text_box = Text (root , height = 3 , width = 300)
btn = Button (root , text = 'Click Me' , fg = "red" , bg = "orange" , height = 1 , width = 100, command = display)
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()




