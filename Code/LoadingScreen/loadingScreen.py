"""
TSA Skill Development Challenge Round B - Software Development
By: Mukund Raman and Leean Zhong

File: loadingScreen.py
Purpose: To provide an initial opening screen to signal that the
         application is loading.
Date: 1/1/2021
Version: 1.0.0
"""

# Imports
from tkinter import *
from PIL import ImageTk,Image


# Function to display the initial loading screen of the application
def displayLoadingScreen():
    #Create Window
    root = Tk()

    #Window dimensions
    # getting screen's height in pixels 
    height = root.winfo_screenheight()  
    # getting screen's width in pixels 
    width = root.winfo_screenwidth()
    root.state("zoomed")

    #Naming window
    root.title("Loading Screen")
    canvas=Canvas(root, width=width, height=height)
    
    #Set background color
    canvas.configure(bg="black")
    canvas.pack()

    #displaying the image
    global img
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\Kids.DESKTOP-2OS06UD\Desktop\Python for TSA\GitHub\CodeAttack\CodeAttack\Resources\Images\TSALogoTransparent.png"))
    canvas.create_image(width/2,height/2, image=img)
    mainloop()

#Run function
displayLoadingScreen()



