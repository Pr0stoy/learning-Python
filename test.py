from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Test")
root.geometry("400x600+700+150")
root.wm_attributes("-alpha",0.7)
root.resizable(False,False)

label = Label(root,text="text",borderwidth=2,relief="raised",background="#FFFFFF")
label.place(x=175,y=275,height=50,width=50)
root.mainloop()