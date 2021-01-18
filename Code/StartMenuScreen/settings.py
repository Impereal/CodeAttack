"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: settings.py
Purpose: To display the game settings
Date: 1/1/2021
Version: 1.0.0
"""

# Library Imports
from tkinter import *

# Function to display a board with the settings
def main(root):
    # Calculate the screen width and height for this mini-window
    scr_height = (root.winfo_screenheight() * 3) / 4
    scr_width = (root.winfo_screenwidth() * 3) / 4

    # Set the window dimensions and position relative to the screen and title the window
    window = Toplevel(width=scr_width, height=scr_height)
    window.geometry(str(int(scr_width)) + 'x' + str(int(scr_height)) + '+' + str(int(scr_width/6)) + '+' + str(int(scr_height/6)))
    window.title("Settings")

# Function to create a slider whose value corresponds to the
# volume of the background music, which can be increased or decreased
# accordingly
def gameAudio():
    pass