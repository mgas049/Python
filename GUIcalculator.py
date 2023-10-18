#Python program to create a simple GUI calculator using Tkinter
# tutorial and code provided by geeksforgeeks.org
# I changed some of the dimensions and added some additional functionality. 

# ***Marc Glass
# ***10/17/2023

#import tkinter module
from tkinter import *

# globally declare the expression var
expression = ""


def press(num):
    # point out the global expression var
    global expression

    # concatenation of string
    expression = expression +str(num)

    # update expression by using set method
    equation.set(expression)


# function to evaluate the final expression 
def equalpress():
    # the try and except statements are used to handle errors
    # code that may generate an error goes inside the try block
    try:
        global expression

        # eval() evaluates the expression and str() converts the results into printable string
        total = str(eval(expression))

        equation.set(total)

        #initialize expression var with empty string
        expression = ""

    # if an error is generated then handle by the except block
    except:

        equation.set(" error ")
        expression = ""


#function to clear the contents of the entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":

    # create the gui window
    gui = Tk()

    # set background color of window
    gui.configure(background="grey")

    #set title of gui window
    gui.title("Simple Calculator")

    # set the configuration of the GUI window
    gui.geometry("530x320")

    # StringVar() is the variable class.
    # Create an instance of this class.
    equation = StringVar()

    # create the 1-line text entry box
    expression_field = Entry(gui, textvariable=equation, font=('courier', 20, 'bold'))
    
    # grid method is used for placing
    #widgets at respective positions in a table-like structure
    
    expression_field.grid(columnspan=4, ipadx=80)


    # create buttons and place at locations inside root window.
    # digits are yellow when pressed
    # signs are orange when pressed
    # decimal is purple when pressed
    # clear is red when pressed
    button1 = Button(gui, text=' 1 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(1), height=3, width=20)
    button1.grid(row=2, column=0)
    
    
    button2 = Button(gui, text=' 2 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(2), height=3, width=20)
    button2.grid(row=2, column=1)
    
    
    
    button3 = Button(gui, text=' 3 ', fg = 'black', bg = 'light blue', activebackground='yellow', 
                     command=lambda: press(3), height=3, width=20)
    button3.grid(row=2, column=2)
    
    
    button4 = Button(gui, text=' 4 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(4), height=3, width=20)
    button4.grid(row=3, column=0)
    
    
    button5 = Button(gui, text=' 5 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(5), height=3, width=20)
    button5.grid(row=3, column=1)
    
    
    button6 = Button(gui, text=' 6 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(6), height=3, width=20)
    button6.grid(row=3, column=2)
    
    
    button7 = Button(gui, text=' 7 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(7), height=3, width=20)
    button7.grid(row=4, column=0)
    
    
    button8 = Button(gui, text=' 8 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(8), height=3, width=20)
    button8.grid(row=4, column=1)
    
    
    button9 = Button(gui, text=' 9 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(9), height=3, width=20)
    button9.grid(row=4, column=2)
    
    
    button0 = Button(gui, text=' 0 ', fg='black', bg='light blue', activebackground='yellow',
                     command=lambda: press(0), height=3, width=20)
    button0.grid(row=5, column=0)


    plus = Button(gui, text=' + ', fg='black', bg='light blue', activebackground='orange',
                     command=lambda: press("+"), height=3, width=10)
    plus.grid(row=2, column=3)


    minus = Button(gui, text=' - ', fg='black', bg='light blue', activebackground='orange',
                     command=lambda: press("-"), height=3, width=10)
    minus.grid(row=3, column=3)


    multiply = Button(gui, text=' * ', fg='black', bg='light blue', activebackground='orange',
                     command=lambda: press("*"), height=3, width=10)
    multiply.grid(row=4, column=3)


    divide = Button(gui, text=' / ', fg='black', bg='light blue', activebackground='orange',
                     command=lambda: press("/"), height=3, width=10)
    divide.grid(row=5, column=3)


    equal = Button(gui, text=' = ', fg='black', bg='light blue', activebackground='green',
                     command=equalpress, height=3, width=20)
    equal.grid(row=5, column=2)


    decimal = Button(gui, text=' . ', fg='black', bg='light blue', activebackground='purple',
                     command=lambda: press("."), height=3, width=20)
    decimal.grid(row=5, column=1)

    # adding the clear button at the bottom, spans 4 columns
    clear = Button(gui, text='Clear', fg='black', bg='light blue', activebackground='red',
                     command=clear, height=3, width=30)
    clear.grid(row=6, column=0, columnspan = 4, sticky= 'WE') 


    
    

    gui.mainloop()
    
