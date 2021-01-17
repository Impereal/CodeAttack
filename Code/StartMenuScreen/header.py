"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: header.py
Purpose: To create a styled header for the start menu screen
         which contains the game's name.
Date: 1/1/2021
Version: 1.0.0
"""

# Imports
from tkinter import *
import sys
import os
import tkinter as tk
import options as op

# Function to create a styled header for the start menu screen,
# used in "startMenuScreen.py"
def createHeader():
    header = Label(op.root, text = "CodeAttack", font =("Century gothic", 48, "bold"), foreground = "lightgrey")
    header.configure(bg = "#3776ab")
    header.place(width = op.centerWidth, y = op.centerHeight/5)


