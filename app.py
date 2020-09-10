from tkinter import *
import parser

root = Tk()
root.title("Calculator")
root.geometry("650x350")

miFrame = Frame(root)
miFrame.pack()

display = Entry(miFrame)
display.grid(row=1, columnspan=6,sticky=W+E)
display.config(bg="orange", justify="right")

i=0
def get_numbers(n):
    global i
    display.insert(i,n)
    i+=1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i,operator)
    i+=operator_length

def delete():
    display.delete(0,END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new = display_state[:-1]
        delete()
        display.insert(0,display_new)
    else:
        delete()
        display.insert(0,'Error')

def calculator():
    display_new = display.get()
    try:
        mass = parser.expr(display_new).compile()
        result = eval(mass)
        delete()
        display.insert(0,result)
    except expression as identifier:
        delete()
        display.insert(0,'Error')

# Numeric Buttom
Button(miFrame,text="1",command=lambda : get_numbers(1)).grid(row=2, column=0,sticky=W+E)
Button(miFrame,text="2",command=lambda : get_numbers(2)).grid(row=3, column=0,sticky=W+E)
Button(miFrame,text="3",command=lambda : get_numbers(3)).grid(row=4, column=0,sticky=W+E)



Button(miFrame,text="4",command=lambda : get_numbers(4)).grid(row=2, column=1,sticky=W+E)
Button(miFrame,text="5",command=lambda : get_numbers(5)).grid(row=3, column=1,sticky=W+E)
Button(miFrame,text="6",command=lambda : get_numbers(6)).grid(row=4, column=1,sticky=W+E)



Button(miFrame,text="7",command=lambda : get_numbers(7)).grid(row=2, column=2,sticky=W+E)
Button(miFrame,text="8",command=lambda : get_numbers(8)).grid(row=3, column=2,sticky=W+E)
Button(miFrame,text="9",command=lambda : get_numbers(9)).grid(row=4, column=2,sticky=W+E)


Button(miFrame,text="AC",command=lambda : delete()).grid(row=5, column=0,sticky=W+E)
Button(miFrame,text="%",command=lambda : get_operation("%")).grid(row=5, column=1,sticky=W+E)
Button(miFrame,text="0").grid(row=5, column=2,sticky=W+E)


Button(miFrame,text="+",command=lambda : get_operation("+")).grid(row=2, column=3,sticky=W+E)
Button(miFrame,text="-",command=lambda : get_operation("-")).grid(row=3, column=3,sticky=W+E)
Button(miFrame,text="*",command=lambda : get_operation("*")).grid(row=4, column=3,sticky=W+E)
Button(miFrame,text="/",command=lambda : get_operation("/")).grid(row=5, column=3,sticky=W+E)


Button(miFrame,text="⤇",command = lambda : undo()).grid(row=2, column=4,sticky=W+E,columnspan=2)
Button(miFrame,text="exp",command=lambda : get_operation("**")).grid(row=3, column=4,sticky=W+E)
Button(miFrame,text="^2",command=lambda : get_operation("**2")).grid(row=3, column=5,sticky=W+E)
Button(miFrame,text="(",command=lambda : get_operation("(")).grid(row=4, column=4,sticky=W+E)
Button(miFrame,text=")",command=lambda : get_operation(")")).grid(row=4, column=5,sticky=W+E)
Button(miFrame,text="=",command= lambda : calculator()).grid(row=5, column=4,sticky=W+E,columnspan=2)


root.mainloop()