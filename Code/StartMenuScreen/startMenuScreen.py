"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: startMenuScreen.py
Purpose: To display a starting menu screen with multiple options
         for the player to choose from before starting the game,
         or to start the game itself.
Date: 1/1/2021
Version: 1.0.0
"""

# Library Imports
from tkinter import *

# Project Imports
from . import options as op
from . import header as he

# Main function to organize all the other components of the screen
def main():
    displayHeader()
    displayOptions()

# Function to display the header of the start menu screen, which is
# created in the file "header.py"
def displayHeader():
    he.createHeader()

# Function to display the different options of the start menu screen,
# which is created in the file "options.py"
def displayOptions():
    op.main()

# Function to be used by other files to return to this screen
def goBack():
    GoBack = Button(op.opRoot, text = "← Go Back", bd = "5")