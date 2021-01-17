"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: tutorial.py
Purpose: To provide a tutorial of the entire game so that the player
         is ready to start playing.
Date: 1/1/2021
Version: 1.0.0
"""

# Imports
from tkinter import *

global root
root = Tk()
root.state("zoomed")
root.title("Tutorials")
centerWidth = root.winfo_screenwidth()
centerHeight = root.winfo_screenheight()
root.configure(bg = "#3776ab")

instructions = Label(root, text = "Instructions", font =("century gothic", 40), foreground = "lightgrey")
instructions.configure(bg = "#3776ab")
instructions.place(width = centerWidth, y = centerHeight/20)

# Function to provide a tutorial of the game
def main():
    pass

# Function to explain about the game background and lore
def explainBG():
    backgroundEx = Label(root, text = "1. The player will complete a quest by defeating all the monsters.", font = ("century gothic", 15), foreground = "black")
    backgroundEx.configure (bg = "#4DC6E2")
    backgroundEx.place(width = centerWidth, y = (centerHeight/20)+90)

# Function to explain about the programming skills that the
# player will learn to use as they progress throughout the game
def explainCoding():
    pass

# Function to explain the different ways of fighting monsters and
# a quick explanation of how to answer the questions to attack
def explainGameMechanics():
    pass

explainBG()
