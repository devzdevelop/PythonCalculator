from tkinter import *
import re

import numexpr

root = Tk()
root.title('Calculator')

# get the user input and place it in the textfield
i = 0


def getVariables(num):
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def calculate():
    entire_string = display.get()
    try:
        #result = sum(map(int, re.findall(r'[+-]?\d+', entire_string)))
        result = numexpr.evaluate(entire_string)
        clearAll()
        display.insert(0, str(result))
    except Exception:
        clearAll()
        display.insert(0, "Error")


def factorial_handler():
    num = int(display.get())
    result = factorial(num)
    clearAll()
    display.insert(0, str(result))

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * (factorial(num - 1))


def clearAll():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string) > 0:
        new_string = entire_string[:-1]
        clearAll()
        display.insert(0, new_string)
    else:
        clearAll()
        display.insert(0, "Error")


# adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# adding buttons to the calculator
Button(root, text="1", command=lambda: getVariables(1)).grid(row=2, column=0)
Button(root, text="2",command=lambda: getVariables(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: getVariables(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: getVariables(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: getVariables(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: getVariables(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: getVariables(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: getVariables(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: getVariables(9)).grid(row=4, column=2)

# adding other buttons to calculator
Button(root, text="AC", command=lambda:clearAll()).grid(row=5, column=0)
Button(root, text="0", command=lambda:getVariables(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda:calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda:get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda:get_operation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda:get_operation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda:get_operation("/")).grid(row=5, column=3)

# adding new operations
Button(root, text="pi", command=lambda:get_operation("* 3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda:get_operation("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda:get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda:get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda:undo()).grid(row=2, column=5)
Button(root, text="x!", command=lambda:factorial_handler()).grid(row=3, column=5)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda:get_operation("^2")).grid(row=5, column=5)


root.mainloop()