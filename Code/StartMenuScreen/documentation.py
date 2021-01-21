"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: documentation.py
Purpose: To provide documentation of the different code blocks
         used within the game with a detailed description of each
         of these blocks.
Date: 1/1/2021
Version: 1.0.0
"""

# Library Imports
from tkinter import *

# Function to create the documentation board and list out each of the
# code blocks
def main(width, height):

    # Calculate the screen width and height for this mini-window
    scr_height = (height * 3) / 4
    scr_width = (width * 3) / 4

    # Set the window dimensions and position relative to the screen and title the window
    window = Toplevel(width = scr_width, height = scr_height)
    window.geometry(str(int(scr_width)) + 'x' + str(int(scr_height)) + '+' + str(int(scr_width * 7 / 18)) + '+' + str(int(scr_height * 7 / 18)))
    window.configure(background = "#5786ab")
    window.title("Documentation")

    # Create the header for this window
    header = Label(window, text = "Documentation", width = 100, font = ("Century Gothic", 48, "bold"), foreground = "lightgray")
    header.configure(bg = "#5786ab")
    header.place(width = scr_width, y = scr_height/15)