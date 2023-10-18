# Clock program that displays a menu with options for time, date and stopwatch. 
# This iteration implements tkinter gui
# also added in a stopwatch for additional functionality. 
# additional buttons also added for future additions.


# Marc Glass
# 10/17/2023
from datetime import datetime
import time
import os
from tkinter import *
from tkinter.messagebox import showinfo


def GUIcalculator():
    GUIcalculator.main()

counter = -1.0
running = False
def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter==-1:             
                display="00.0"
            else:
                display=str(counter)

            lbl['text']=display    
            
            lbl.after(1000, count)    
            counter += 1.0
    count()      



def startTime(lbl):
    global running
    running=True
    counter_label(lbl)
    #startbtn['state']='disabled'
    #stopbtn['state']='normal'
    #resetbtn['state']='normal'




def endTime():
    global running
    #startbtn['state']='normal'
    #stopbtn['state']='disabled'
    #resetbtn['state']='normal'
    running = False



def resetTime(lbl):
    global counter
    counter=-1.0
    if running==False:      
        #reset['state']='disabled'
        lbl['text']='00.0'
    else:                          
        lbl['text']=''



# defines the stopwatch function     ****FIX ME***: start, stop and reset are not being disabled
def stopWatch():
    #creates secondary window  
    stopWatch = Tk()
    stopWatch.configure(background = "grey")
    stopWatch.title("Stopwatch")
    stopWatch.geometry('600x480')
    stopWatch.resizable(0,0)
    
    lbl = Label(stopWatch, text="00.0", fg="black", bg='grey', font="Verdana 40 bold")
    lbl.grid(row=1, column=0)
    
    label_msg = Label(stopWatch, text="seconds", fg="black", bg='grey', font="Verdana 10 bold")
    label_msg.grid(row=2, column=0)
    
    
    #start button
    startbtn = Button(stopWatch, text="Start", fg='black', bg='light blue',
                   command=lambda:startTime(lbl), height=3, width=10)
    startbtn.grid(row=3, column=0)

    #stop button
    stopbtn = Button(stopWatch, text="Stop", fg='black', bg='light blue',
                   command=endTime, height=3, width=10)
    stopbtn.grid(row=4, column=0)

    #reset button
    resetbtn = Button(stopWatch, text="Reset", fg='black', bg='light blue',
                   command=lambda:resetTime(lbl), height=3, width=10)
    resetbtn.grid(row=5, column=0)

    

    
    

# Prints the current date
def getDate():
    showinfo("Date", datetime.now().strftime('%Y-%m-%d'))
    
    
    
# prints the current time
def getTime():
    showinfo("Time", datetime.now().strftime('%H:%M:%S'))
    
   

#placeholder for next feature
def testOne():
    showinfo("Test1", "This is holding a spot for an upcoming feature")
    

#placeholder for next feature
def testTwo():
    showinfo("Test2", "This is holding a spot for an upcoming feature")

#placeholder for next feature
def testThree():
    showinfo("Test3", "This is holding a spot for an upcoming feature")

#placeholder for next feature
def testFour():
    showinfo("Test4", "This is holding a spot for an upcoming feature")


# define main
def main():
    # create window
    gui = Tk()
    
    # set background color of window
    gui.config(background="grey")

    # set title of window
    gui.title("Clock by Marc Glass")

    # configuration of the window
    gui.geometry("150x400")

    #window is not resizable
    gui.resizable(0,0)
    

    #create buttons
    time = Button(gui, text='Time', fg='black', bg='light blue', activebackground='yellow',
                     command=getTime, height=3, width=20)
    time.grid(row=1, column=0)


    date = Button(gui, text='Date', fg='black', bg='light blue', activebackground='yellow',
                     command=getDate, height=3, width=20)
    date.grid(row=2, column=0)


    stopwatch = Button(gui, text='Stopwatch', fg='black', bg='light blue', activebackground='yellow',
                     command=stopWatch, height=3, width=20)
    stopwatch.grid(row=3, column=0)


    test1 = Button(gui, text='Test1', fg='black', bg='light blue', activebackground='yellow',
                     command=testOne, height=3, width=20)
    test1.grid(row=4, column=0)
    

    test2 = Button(gui, text='Test2', fg='black', bg='light blue', activebackground='yellow',
                     command=testTwo, height=3, width=20)
    test2.grid(row=5, column=0)

    test3 = Button(gui, text='Test3', fg='black', bg='light blue', activebackground='yellow',
                     command=testThree, height=3, width=20)
    test3.grid(row=6, column=0)

    test4 = Button(gui, text='Test4', fg='black', bg='light blue', activebackground='yellow',
                     command=testFour, height=3, width=20)
    test4.grid(row=7, column=0)


    
        
    

    
    

if __name__ == "__main__":
    main()
