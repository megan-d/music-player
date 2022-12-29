from tkinter import *
import pygame
import os

player = Tk()

# Configure appearance of GUI
player.title("Python Music Player")
player.geometry("800x600")


# Initialize pygame mixer module for loading and playing sounds
pygame.mixer.init()


# Put everything on the display and respond to user input until the program terminates
player.mainloop()
