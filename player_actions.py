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


def load_music():
    global current_song
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        for song in os.listdir(path):
            # split the file extension from the filename
            name, ext = os.path.splitext(song)
            if ext == ".mp3":
                all_songs.append(song)
                songs_list.insert(END, song)

    # current_song_index = songs_list.index(ACTIVE)
    songs_list.selection_set(0)
    current_song = all_songs[songs_list.curselection()[0]]


def get_active_song_index():
    active_song = songs_list.index(ACTIVE)
    return active_song


def play_song():
    global current_song
    # song_info = songs_list.get(ACTIVE)
    mixer.music.load(current_song)
    mixer.music.play()
    music_label.config(text=current_song[0:-4])


def pause_music():
    global is_paused
    mixer.music.pause()


def stop_music():
    global is_paused
    mixer.music.stop()


def next_song():
    global current_song
    try:
        songs_list.selection_clear(0, END)
        songs_list.selection_set(all_songs.index(current_song) + 1)
        current_song = all_songs[songs_list.curselection()[0]]
        mixer.music.load(current_song)
        mixer.music.play()
        music_label.config(text=current_song[0:-4])

    except (Exception):
        pass


# def previous_song():
#     global current_song

#     try:
#         songs_list.selection_clear(0, END)
#         songs_list.selection_set(all_songs.index(current_song) - 1)
#         current_song = all_songs[songs_list.curselection()[0]]
#         play_music()

#     except (Exception):
#         pass
