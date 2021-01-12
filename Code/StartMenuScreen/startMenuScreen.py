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

# Imports
from tkinter import *
import sys
import os
import tkinter as tk
from options import *
import options as op
import header as he
import quitScreen as qu

# Main function to organize all the other components of the screen
def main():
    setBackground()
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
    GoBack = Button(root, text = "← Go Back", bd = "5")

######################################################
### OTHER FUNCTIONS TBD (including setBackground)  ###
######################################################

# Function to set the background of the start menu screen
def setBackground():
    op.root.configure(bg="#3776ab")

main()

