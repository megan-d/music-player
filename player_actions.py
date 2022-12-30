import os
from tkinter import filedialog
from tkinter import *
from pygame import mixer

root = Tk()

# Create listbox
songs_list = Listbox(root, bg="white", fg="black", width=800, height=30, bd=0)

songs_list.pack()

music_label = Label(root, text="", font=("arial", 16, "bold"), fg="black", bg="white")
music_label.place(x=20, y=480)

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
        songs_list.insert(END, song)

    songs_list.selection_set(0)
    current_song = all_songs[songs_list.curselection()[0]]


def play_song():
    global current_song, is_paused
    song_info = songs_list.get(ACTIVE)
    if not is_paused:
        mixer.music.load(os.path.join(root.directory, current_song))
        mixer.music.play()
        music_label.config(text=song_info[0:-4])
    else:
        mixer.music.unpause()
        is_paused = False


def pause_music():
    global is_paused
    mixer.music.pause()
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
