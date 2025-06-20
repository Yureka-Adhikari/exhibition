import tkinter as tk
from tkinter import *
import subprocess
import sys
import os

root = Tk()
root.geometry('700x700')
root.title("ICT Meet Main Menu")
root.configure(bg="#454587")

Label(root, text="The Main Menu For Our Projects!", font=("Times New Roman", 18), bg="#E2E2FF", fg="#454587").pack(pady=20)

def open_order():
    subprocess.run(["python", "table.py"])

def open_rock():
    subprocess.run(["python", "rock paper scissors.py"])

def open_diary():
    subprocess.run(["python", "diary.py"])

def open_space():
    subprocess.run(
        [sys.executable, "game.py"],
        cwd=os.path.join(os.getcwd(), "space invaders")
    )

def load_image(path, subsample_factor):
    img = PhotoImage(file=path)
    img = img.subsample(subsample_factor, subsample_factor)
    return img

restraunt_img = load_image("restraunt.png", 5)
rock_img = load_image("Rock Paper Scissors.png", 3)
diary_img = load_image("diary.png", 5)
space_img = load_image("Space Invaders.png", 5)

button_frame = Frame(root, bg="#e6e6fa")
button_frame.pack(expand=True, fill=BOTH, padx=30, pady=30)

buttons = [
    {"image": restraunt_img, "text": "Restraunt", "command": open_order},
    {"image": rock_img, "text": "Rock Paper Scissors", "command": open_rock},
    {"image": diary_img, "text": "Diary", "command": open_diary},
    {"image": space_img, "text": "Space Invaders", "command": open_space},
]

for i in range(4):
    btn = Button(
        button_frame,
        image=buttons[i]["image"],
        text=buttons[i]["text"],
        compound="top",
        width=120,
        height=120,
        command=buttons[i]["command"]
    )
    btn.grid(row=i//2, column=i%2, padx=30, pady=30, sticky="nsew")

for i in range(2):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(2):
    button_frame.grid_rowconfigure(i, weight=1)

root.mainloop()