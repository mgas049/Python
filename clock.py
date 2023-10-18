# Clock program that displays a menu with options for time, date and stopwatch. 
# Next iteration will implement tkinter gui

# Marc Glass
# 10/17/2023
from datetime import datetime
import time
import os

#defines the time converter for the stopwatch
def timeConvert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("*******************************\n" 
          "*          Time Lapsed:       *\n"
          "*                             *\n"
          "*          {0}:{1}:{2}           *\n"
          "*                             *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************\n\n".format(int(hours),int(mins),round(sec,2)))

# defines the stopwatch function
def stopWatch():
    # starts the stopwatch
    input("*******************************\n" 
          "*          Stopwatch          *\n"
          "*                             *\n"
          "*    Press 'enter' to start   *\n"
          "*                             *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************\n\n")
    startTime = time.time()

    input("*******************************\n" 
          "*          Stopwatch          *\n"
          "*                             *\n"
          "*    Press 'enter' to stop    *\n"
          "*                             *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************\n\n")
    endTime = time.time()

    timeLapsed = endTime - startTime
    timeConvert(timeLapsed)
    

# Prints the current date
def getDate():
    x = datetime.now().strftime('%Y-%m-%d')
    print("*******************************\n" 
          "*           Date              *\n"
          "*                             *\n"
          "*         " + x + "          *\n"
          "*                             *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************\n\n")
    

# prints the current time
def getTime():
    x = datetime.now().strftime('%H:%M:%S')
    
    print("*******************************\n" 
          "*           TIME              *\n"
          "*                             *\n"
          "*         " + x + "            *\n"
          "*                             *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************\n\n")

# outputs message for invalid input
def invalidInput():
    print("*******************************\n" 
          "*                             *\n"
          "*                             *\n"
          "*       Invalid Input!        *\n"
          "*                             *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************\n\n")

#prints the main menu
def mainMenu():
    
    print("*******************************\n" 
          "*   Please Choose One:        *\n"
          "*                             *\n"
          "*   't' for current time      *\n"
          "*   'd' for current date      *\n"
          "*   's' for stopwatch         *\n"
          "*   'x' to exit               *\n"
          "*                             *\n"
          "*******************************\n")


    
# define main
def main():
    
    userIn = ""
    while userIn != "x":
        mainMenu()
        userIn = input("")

        if userIn == 't':
            getTime()
        if userIn == 'd':
            getDate()
        if userIn == 's':
            stopWatch()
        if userIn != 'x' and userIn != 'd' and userIn != 't' and userIn != 's':
            invalidInput()

        
    print("*******************************\n" 
          "*                             *\n"
          "*                             *\n"
          "*       Thanks for using!     *\n"
          "*          Goodbye!           *\n"
          "*                             *\n"
          "*                             *\n"
          "*******************************")            

        
    

    
    

if __name__ == "__main__":
    main()
