from tkinter import *
#GLOBAL VAR
fn = 0
sn = 0
op = ""
#Setup
##init
root = Tk()
root.title("Calculator")
##Entry init
entry = Entry(root, width = 45, borderwidth = 5)
entry.grid(row = 0, column = 0,columnspan = 4)

#utils
def get_value(number):
    temp = entry.get()
    if temp in arritm:
        entry.delete(0, END)
    numbers = []
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+ str(number))

    
def get_math(oper):
    global fn
    global op
    temp = entry.get()
    fn = int(temp)
    first_number = entry.get()
    entry.delete(0,END)
    entry.insert(0, arritm[oper])
    op = arritm[oper]

    
def clear():
    entry.delete(0, END)


def result():
    global fn
    global sn
    global op
    temp = entry.get()
    sn = int(temp)
    entry.delete(0, END)
    if op == "+":
        entry.insert(0, fn+sn)
    elif op == "-":
        entry.insert(0, fn-sn)
    elif op == "x":
        entry.insert(0, fn*sn)
    elif op == "/":
        entry.insert(0, fn/sn)
    
   
#Creating buttons 
##Numbers
number = 1 
for row in range(3,0, -1):
    for column in range(0, 3): 
        button = Button(root, text=number, pady =30, padx = 30, command = lambda number = number: get_value(number)).grid(row = row, column = column)
        number += 1
button0 = Button(root, text="0", pady =30, padx = 30, command =lambda number = number: get_value(0)).grid(row = 4, column = 1)
button_clear  = Button(root, text="C", pady =30, padx = 30, command =clear).grid(row = 4, column = 0)
button_equal  = Button(root, text="=", pady =30, padx = 30, command =result).grid(row = 4, column = 2)
##Aritmetic
arritm= ["+","-","x","/"]
i = 0
for row in range(1,5):
    button = Button(root, text=arritm[i], pady =30, padx = 30, command = lambda i = i:get_math(i)).grid(row = row, column = 3)
    i+= 1


        


 



    
root.mainloop()


    

