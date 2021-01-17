"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: options.py
Purpose: To create all the different options of the starting
         menu screen.
Date: 1/1/2021
Version: 1.0.0
"""

# Imports
from tkinter import *
import sys
import os
import tkinter as tk

# Function to create the play option for the options,
# linking to the gameplay screen when clicked
global root
root = Tk()
root.state("zoomed")
root.title("Start Menu")
centerWidth = root.winfo_screenwidth()
centerHeight = root.winfo_screenheight()

def playlink():
     os.system("python gamePlayScreen.py")
def playOption():
    Play = Button(root, text = "Play", bd = "2", width = "20", command = playlink())
    Play.configure(font=('Century gothic', 12),foreground='black')
    Play.place(x = centerWidth/2.35, y = centerHeight/2.5)


# Function to create the lessons and documentation option,
# opening the lessons board when clicked
def lessonslink():
     os.system("lessons.py")
def lessonsOption():
    Lessons = Button(root, text = "Lessons & Documents", bd = "2", width= "20", command= lessonslink())
    Lessons.configure(font=('Century gothic', 12),foreground='black')
    Lessons.place(x = centerWidth/2.35, y = (centerHeight/2.5)+40)
    

# Function to create the settings option, opening the settings
# board when clicked
def settingslink():
    os.system("python settings.py")
def settingsOption():
    Settings = Button(root, text = "Settings", bd = "2", width ="20", command = settingslink())
    Settings.configure(font=('Century gothic', 12),foreground='black')
    Settings.place(x = centerWidth/2.35, y = (centerHeight/2.5)+80)

# Function to create the quit option, closing the program when
# clicked
def quitlink():
    os.system("python quit.py")
def quitOption():
    Quit = Button(root, text = "Quit", bd = "2", width = "20", command = root.destroy)
    Quit.configure(font=('Century gothic', 12),foreground ='black')
    Quit.place(x = centerWidth/2.35, y = (centerHeight/2.5)+120)

# Function to create a component with all the different
# options for the starting menu screen
def main():
    playOption()
    lessonsOption()
    settingsOption()
    quitOption()



    
    
