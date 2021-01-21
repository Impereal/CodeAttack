"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: lessons.py
Purpose: To display a brief overview of all the educational
         programming lessons covered within the game.
Date: 1/1/2021
Version: 1.0.0
"""

# Library Imports
from tkinter import *

# Relative Imports
from . import documentation

# Function to display the lessons board with all of the lessons
def displayLessons(root):
    # Calculate the screen width and height for this mini-window
    scr_height = (root.winfo_screenheight() * 3) / 4
    scr_width = (root.winfo_screenwidth() * 3) / 4

    # Set the window dimensions and position relative to the screen and title the window
    window = Toplevel(width = scr_width, height = scr_height)
    window.geometry(str(int(scr_width)) + 'x' + str(int(scr_height)) + '+' + str(int(scr_width/6)) + '+' + str(int(scr_height/6)))
    window.configure(background = "#4776ab")
    window.title("Lessons")

    # Create the header for this window
    header = Label(window, text = "Lessons", width = 100, font = ("Century Gothic", 60, "bold"), foreground = "lightgray")
    header.configure(bg = "#4776ab")
    header.place(width = scr_width, y = scr_height/15)

    # Setup documentation button
    documentationButton(window, scr_width, scr_height)

    # Create all the lesson overviews
    lesson1Overview(window, scr_width, scr_height)
    lesson2Overview(window, scr_width, scr_height)
    lesson3Overview(window, scr_width, scr_height)
    lesson4Overview(window, scr_width, scr_height)

# Function to create and display the overview of the four lessons
def lesson1Overview(window, scr_width, scr_height):
    pass
def lesson2Overview(window, scr_width, scr_height):
    pass
def lesson3Overview(window, scr_width, scr_height):
    pass
def lesson4Overview(window, scr_width, scr_height):
    pass

# Function to create the documentation button to open a new window
# for the documentation
def documentationButton(window, scr_width, scr_height):
    DocsButton = Button(window, text = "Show Documentation", bd = scr_width, command = lambda: documentation.main(scr_width, scr_height))
    DocsButton.configure(font = ('Calibri', 20), foreground = 'black', highlightbackground = 'lightgray')
    DocsButton.place(width = (scr_width * 3) / 4, height = 75, x = scr_width/8, y = scr_height/1.15)