import tkinter as tk
from tkinter import Tk, Button, Label
import subprocess
import sys
import os


root = Tk()
root.geometry('400x400')
root.title("ICT Meet Main Menu")

Label(root, text="Welcome to ICT Meet!", font=("Arial", 18)).pack(pady=20)

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
    
        
Button(root, text="Table Order", width=25, height=2, command=open_order).pack(pady=10)
Button(root, text="Rock Paper Scissors", width=25, height=2, command=open_rock).pack(pady=10)
Button(root, text="Diary", width=25, height=2, command=open_diary).pack(pady=10)
Button(root, text="Space Invaders", width=25, height=2, command=open_space).pack(pady=10)
Button(root, text="Quit", width=25, height=2, command=root.quit).pack(pady=10)

root.mainloop()