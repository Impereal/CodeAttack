"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: options.py
Purpose: To create all the different options of the starting
         menu screen.
Date: 1/1/2021
Version: 1.0.0
"""

# Library Imports
from tkinter import *
import sys
import os
import tkinter as tk

# Relative Imports
from ..GamePlayScreen import gamePlayScreen
from . import lessons
from . import settings

# Create the root window for the options
# and set the window properties
opRoot = Tk()
opRoot.state("zoomed")
opRoot.title("Start Menu")
centerWidth = opRoot.winfo_screenwidth()
centerHeight = opRoot.winfo_screenheight()

# Create and configure the Canvas
canvas=Canvas(opRoot, width=centerWidth, height=centerHeight)
canvas.configure(bg="#3776ab")
canvas.pack()

# Functions to create the play option for the options,
# linking to the gameplay screen when clicked
def playOption():
    global opRoot
    Play = Button(opRoot, text = "Play", bd = "2", width = "20", command = gamePlayScreen.main)
    Play.configure(font=('Century gothic', 12),foreground='black')
    Play.place(width = (centerWidth * 3) / 4, height = 100, x = centerWidth/8, y = centerHeight/3)


# Function to create the lessons and documentation option,
# opening the lessons board when clicked
def lessonsOption():
    global opRoot
    Lessons = Button(opRoot, text = "Lessons & Documents", bd = "2", width= "20", command = lambda: lessons.displayLessons(opRoot))
    Lessons.configure(font=('Century gothic', 12),foreground='black')
    Lessons.place(width = (centerWidth * 3) / 4, height = 100, x = centerWidth/8, y = (centerHeight/3)+150)
    

# Function to create the settings option, opening the settings board when clicked
def settingsOption():
    Settings = Button(opRoot, text = "Settings", bd = "2", width ="20", command = lambda: settings.main(opRoot))
    Settings.configure(font=('Century gothic', 12),foreground='black')
    Settings.place(width = (centerWidth * 3) / 4, height = 100, x = centerWidth/8, y = (centerHeight/3)+300)

# Function to create the quit option, closing the program when clicked
def quitOption():
    global opRoot
    Quit = Button(opRoot, text = "Quit", bd = "2", width = "20", command = quit)
    Quit.configure(font=('Century gothic', 12),foreground ='black')
    Quit.place(width = (centerWidth * 3) / 4, height = 100, x = centerWidth/8, y = (centerHeight/3)+450)

# Function to create a component with all the different
# options for the starting menu screen
def main():
    playOption()
    lessonsOption()
    settingsOption()
    quitOption()
    
    global opRoot
    opRoot.mainloop()