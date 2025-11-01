import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os


pygame.mixer.init()


root = tk.Tk()
root.title("Музыкальный плеер")
root.geometry("400x400")

root.resizable(False, False)

playlist = []    
current_song = "" 
paused = False


def add_songs():
   
    files = filedialog.askopenfilenames(
        title="Выберите песни",
        filetypes=[("Аудиофайлы", "*.mp3 *.wav")]
    )
    for file in files:
        playlist.append(file)
        song_list.insert(tk.END, os.path.basename(file))

def play_song():
 
    global current_song, paused
    try:
        selected = song_list.curselection()
        if selected:
            current_song = playlist[selected[0]]
            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play()
            paused = False
            label_song.config(text=f"▶️ Сейчас играет: {os.path.basename(current_song)}")
        else:
            messagebox.showinfo("Плеер", "Выберите песню из списка!")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def pause_song():
  
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
        label_song.config(text="⏸️ Пауза")
    else:
        pygame.mixer.music.unpause()
        paused = False
        label_song.config(text=f"▶️ Сейчас играет: {os.path.basename(current_song)}")

def stop_song():
   
    pygame.mixer.music.stop()
    label_song.config(text="⏹️ Остановлено")

def set_volume(val):
 
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)


label_song = tk.Label(root, text="Файл не выбран", wraplength=350)
label_song.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_add = tk.Button(frame_buttons, text="➕ Добавить", command=add_songs, width=10)
btn_add.grid(row=0, column=0, padx=5)

btn_play = tk.Button(frame_buttons, text="▶️ Play", command=play_song, width=10)
btn_play.grid(row=0, column=1, padx=5)

btn_pause = tk.Button(frame_buttons, text="⏸️ Pause", command=pause_song, width=10)
btn_pause.grid(row=0, column=2, padx=5)

btn_stop = tk.Button(frame_buttons, text="⏹️ Stop", command=stop_song, width=10)
btn_stop.grid(row=0, column=3, padx=5)


song_list = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
song_list.pack(pady=10)


volume_frame = tk.Frame(root)
volume_frame.pack(pady=10)

tk.Label(volume_frame, text="Громкость").pack(side=tk.LEFT)
volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_slider.set(70)  
volume_slider.pack(side=tk.LEFT)


root.mainloop()
