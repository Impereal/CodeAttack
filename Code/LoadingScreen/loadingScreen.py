"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: loadingScreen.py
Purpose: To provide an initial opening screen to signal that the
         application is loading.
Date: 1/1/2021
Version: 1.0.0
"""

# Library Imports
from tkinter import *
from time import time

# Function to destroy the root window for the
# loading screen and open the starting menu screen
# once the application has loaded
def openStartMenu():
    from ..StartMenuScreen import startMenuScreen
    global root
    root.withdraw()
    startMenuScreen.main()
    
# Function to display the initial loading screen of the application
def displayLoadingScreen():
    # Creates Window and sets destruction time
    global root
    root = Tk()
    root.after(5000, openStartMenu)

    # Setup of dimensions and other window properties
    height = root.winfo_screenheight()  
    width = root.winfo_screenwidth()
    root.state("zoomed")
    root.title("Loading Screen")

    # Creation and configuration of Canvas
    canvas=Canvas(root, width=width, height=height)
    canvas.configure(bg="black")
    canvas.pack()

    # Displays the TSA Logo Image
    img = PhotoImage(master=canvas, file=r"./Resources/Images/TSALogoTransparent.png")
    canvas.create_image(width/2,height/2, image=img)

    # Starts the window
    root.mainloop()



