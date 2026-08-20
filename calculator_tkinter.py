from tkinter import *
from tkinter import ttk
import re
root = Tk()
root.geometry("300x460+800+250")
root.wm_attributes("-alpha",0.8)
# root.resizable(False,False)
root.config(background="#4b4747")
buttons = [
    ["7","8","9","+"],
    ["4","5","6","-"],
    ["1","2","3","*"],
    
]

def solve():
    try:    
        problem = entry.get()
        clear()
        problem_split_number = re.split(r"[+*/-]",problem)
        problem_split_operator = re.findall(r"[+*/-]",problem)
        if problem[0] == "-":
            if problem_split_operator[1] == "/" and problem_split_number[2] == "0":
                result = "are you stupid?"
            elif problem_split_operator[1] == "*":
                result = -1*(float(problem_split_number[1]))*float(problem_split_number[2])
            elif problem_split_operator[1] == "+":
                result = (-1*(float(problem_split_number[1])))+float(problem_split_number[2])
            elif problem_split_operator[1] == "-":
                result = -1*(float(problem_split_number[1]))-float(problem_split_number[2])
            elif problem_split_operator[1] == "/":
                result = -1*(float(problem_split_number[1]))/float(problem_split_number[2])
        else:    
            if problem_split_operator[0] == "/" and problem_split_number[1] == "0":
                result = "are you stupid?"  
            elif problem_split_operator[0] == "*":
                result = float(problem_split_number[0])*float(problem_split_number[1])
            elif problem_split_operator[0] == "+":
                result = float(problem_split_number[0])+float(problem_split_number[1])
            elif problem_split_operator[0] == "-":
                result = float(problem_split_number[0])-float(problem_split_number[1])
            elif problem_split_operator[0] == "/":
                result = float(problem_split_number[0])/float(problem_split_number[1])
        entry.insert(0,f"{result:.10f}".rstrip("0").rstrip("."))  
    except:
        entry.insert(0,"you've done smth wrong")

def enter_num(value):
    entry.insert(END,value)

def clear():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

entry = Entry(root,background="white",font = ("Arial",20),justify="right", insertofftime=0)
entry.grid(row=0, column=0, columnspan=4, padx=(10, 15), pady=10, sticky="we")
entry.focus_set()

for row_indx,row in enumerate(buttons):
    for col_indx, text in enumerate(row):
        root.grid_columnconfigure(col_indx, weight=1) 
        btn = Button(
            root,
            text=text,
            font=("Arial",10),
            width=4,
            height=4,
            command= lambda value=text: enter_num(value),
        )
        btn.grid(row=row_indx+1,column=col_indx,padx=2,pady=2)

btn_backspace = Button(
    root,
    text = "Back",
    font = ("Arial",10),
    width=4,
    height=4,
    command = backspace,
)
btn_backspace.grid(row=4,column=0,padx=2,pady=2)

btn_dot = Button(
    root,
    text=".",
    font=("Arial",10),
    width=4,
    height=4,
    command= lambda: enter_num("."),
)
btn_dot.grid(row=4,column=1,padx=2,pady=2)

btn_division = Button(
    root,
    text="/",
    font=("Arial",10),
    width=4,
    height=4,
    command= lambda: enter_num("/"),
)
btn_division.grid(row=4,column=3,padx=2,pady=2)

btn_zero = Button(
    root,
    text="0",
    font=("Arial",10),
    width=4,
    height=4,
    command= lambda: enter_num("0"),
)
btn_zero.grid(row=4,column=2,padx=2,pady=2)

btn_clear = Button(
    root,
    text="C",
    font=("Arial",10),
    width=4,
    height=4,
    command= clear,
)
btn_clear.grid(row=5,column=0,padx=2,pady=2)

btn_enter = Button(
    root,
    text="=",
    font=("Arial",10),
    width=4,
    height=4,
    command= solve,
)
btn_enter.grid(row=5,column=1,padx=2,pady=2)

root.bind("<Return>", lambda e: solve())
root.bind("<Escape>", lambda e: backspace())



root.mainloop()