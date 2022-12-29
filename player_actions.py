import os
from tkinter import filedialog
from tkinter import *
import pygame

root = Tk()

# Create listbox
songs_list = Listbox(root, bg="black", fg="white", width=800, height=30)

songs_list.pack()

all_songs = []
current_song = None
is_paused = False


def load_music():
    global all_songs, current_song
    root.directory = filedialog.askdirectory()
    for song in os.listdir(root.directory):
        # split the file extension from the filename
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            all_songs.append(song)

    for song in all_songs:
        songs_list.insert("end", song)

    songs_list.selection_set(0)
    current_song = all_songs[songs_list.curselection()[0]]


def play_music():
    global current_song, is_paused
    if not is_paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        is_paused = False


def pause_music():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True


def next():
    global current_song

    try:
        songs_list.selection_clear(0, END)
        songs_list.selection_set(all_songs.index(current_song) + 1)
        current_song = all_songs[songs_list.curselection()[0]]
        play_music()

    except (Exception):
        pass


def previous():
    global current_song

    try:
        songs_list.selection_clear(0, END)
        songs_list.selection_set(all_songs.index(current_song) - 1)
        current_song = all_songs[songs_list.curselection()[0]]
        play_music()

    except (Exception):
        pass
