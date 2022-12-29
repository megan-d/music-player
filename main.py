from tkinter import filedialog
from tkinter import *
import pygame
import os
from player_actions import (
    load_music,
    root,
    all_songs,
    current_song,
    is_paused,
    play_music,
    pause_music,
    next,
    previous,
    songs_list,
)


# Configure appearance of GUI
root.title("Python Music Player")
root.geometry("800x800+100+100")

# Create menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

organizer_menu = Menu(menu_bar, tearoff=False)
organizer_menu.add_command(label="Select a Folder", command=load_music)
menu_bar.add_cascade(label="Select Music", menu=organizer_menu)

# Initialize pygame mixer module for loading and playing sounds
pygame.mixer.init()


# Populate buttons in GUI
open_button_frame = Frame(root)
open_button_frame.pack()
open_button = Button(
    open_button_frame,
    text="Select Music",
    command=load_music,
    pady=10,
    borderwidth=0,
    bd=0,
    highlightthickness=0,
)
open_button.grid()

play_btn_png = PhotoImage(file="play-button.png")
pause_btn_png = PhotoImage(file="pause-button.png")
next_btn_png = PhotoImage(file="play-next.png")
prev_btn_png = PhotoImage(file="play-previous.png")

controls_frame = Frame(root)
controls_frame.pack()

play_btn = Button(
    controls_frame,
    image=play_btn_png,
    borderwidth=0,
    bd=0,
    highlightthickness=0,
    command=play_music,
    padx=0,
    pady=0,
)
pause_btn = Button(
    controls_frame,
    image=pause_btn_png,
    borderwidth=0,
    highlightthickness=0,
    command=pause_music,
)
next_btn = Button(
    controls_frame,
    image=next_btn_png,
    borderwidth=0,
    highlightthickness=0,
    command=next,
)
prev_btn = Button(
    controls_frame,
    image=prev_btn_png,
    borderwidth=0,
    highlightthickness=0,
    command=previous,
)

prev_btn.grid(row=0, column=0, padx=10, pady=10)
play_btn.grid(row=0, column=1, padx=10, pady=10)
pause_btn.grid(row=0, column=2, padx=10, pady=10)
next_btn.grid(row=0, column=3, padx=10, pady=10)

# Put everything on the display and respond to user input until the program terminates
root.mainloop()
