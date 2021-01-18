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
    window = Toplevel(width=scr_width, height=scr_height)
    window.geometry(str(int(scr_width)) + 'x' + str(int(scr_height)) + '+' + str(int(scr_width/6)) + '+' + str(int(scr_height/6)))
    window.title("Lessons")

# Function to open the documentation board once the 'Show Docu-
# mentation' button is clicked
def openDocs():
    pass