from tkinter import *
from pygame import mixer
import os
from player_actions import (
    load_music,
    root,
    play_song,
    pause_music,
    songs_list,
    next_song,
    previous_song,
)


# Configure appearance of GUI
root.title("Python Music Player")
root.geometry("800x800+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

# Create menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

organizer_menu = Menu(menu_bar, tearoff=False)
organizer_menu.add_command(label="Select a Folder", command=load_music)
menu_bar.add_cascade(label="Select Music", menu=organizer_menu)

# Initialize pygame mixer module for loading and playing sounds
mixer.init()


# Populate buttons in GUI
open_button = Button(
    root,
    text="Select Music",
    command=load_music,
    width=15,
    height=2,
    font=("helvetica", 14, "bold"),
    fg="black",
    bg="#21b3de",
    borderwidth=0,
    highlightthickness=0,
)
open_button.place(x=345, y=520)

play_btn_png = PhotoImage(file="play-button.png")
pause_btn_png = PhotoImage(file="pause-button.png")
next_btn_png = PhotoImage(file="play-next.png")
prev_btn_png = PhotoImage(file="play-previous.png")

play_btn = Button(
    root,
    image=play_btn_png,
    bd=0,
    bg="#0f1a2b",
    command=play_song,
)
pause_btn = Button(
    root,
    image=pause_btn_png,
    borderwidth=0,
    highlightthickness=0,
    command=pause_music,
)
next_btn = Button(
    root,
    image=next_btn_png,
    borderwidth=0,
    highlightthickness=0,
    command=next_song,
)
prev_btn = Button(
    root,
    image=prev_btn_png,
    borderwidth=0,
    highlightthickness=0,
    command=previous_song,
)

prev_btn.place(x=100, y=600)
play_btn.place(x=250, y=600)
pause_btn.place(x=400, y=600)
next_btn.place(x=550, y=600)

scroll = Scrollbar()

# Put everything on the display and respond to user input until the program terminates
root.mainloop()
