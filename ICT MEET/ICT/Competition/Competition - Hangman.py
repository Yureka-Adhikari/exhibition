import tkinter as tk
import random
from tkinter import messagebox
    
def word_choose():
    listOfWords = ["Apple", "Eyes", "Laptop", "Desk", "Calculator", "White Board", "Notebook", "Subject"]
    
    hangman_word = random.choice(listOfWords)
    return hangman_word.upper()

def check_letter():
    global wrong_guesses, guessed_letters
    guessed_letter = letter_entry.get().upper().strip()
    
    if guessed_letter in guessed_letters:
        messagebox.showinfo("Repeated Guess", "You already guessed that letter!")
        letter_entry.delete(0, tk.END)
        return
        
    guessed_letters.add(guessed_letter)
    guessed_display.set("Guessed letters: " + " ".join(sorted(guessed_letters)))

    if guessed_letter in hangman_word:
        current = display_word.get().replace(" ", "")
        new_display = []
        for i, ch in enumerate(hangman_word):
            if ch == guessed_letter:
                new_display.append(guessed_letter)
            else:
                new_display.append(current[i])
        display_word.set(" ".join(new_display))

        if "_" not in "".join(new_display):
            messagebox.showinfo("You won!", "Congratulations — you guessed the word!")
    else:
        wrong_guesses += 1
        if wrong_guesses == 1:
            head = display_stickman.create_oval(50, 20, 90, 60)
        elif wrong_guesses == 2:
            display_stickman.create_line(70, 60, 70, 140)
        elif wrong_guesses == 3:
            display_stickman.create_line(70, 80, 120, 100)
        elif wrong_guesses == 4:
            display_stickman.create_line(70, 80, 20, 100)
        elif wrong_guesses == 5:
            display_stickman.create_line(70, 140, 120, 180)
        elif wrong_guesses == 6:
            display_stickman.create_line(70, 140, 20, 180)
            messagebox.showinfo("Game Over", f"You lost! The word was: {hangman_word}")

    letter_entry.delete(0, tk.END) 
        
hangman_word = word_choose()     
root = tk.Tk()
root.title("🎮 Hangman Game")
root.configure(bg="#EAB3B3")

main_frame = tk.Frame(root, bg="#EAB3B3", relief="ridge", bd=3)
main_frame.pack(padx=10, pady=10, fill="both", expand=True)

title_frame = tk.Frame(main_frame, bg="#EAB3B3")
title_frame.pack(pady=10, fill="x")

tk.Frame(title_frame, height=3, bg="#640303").pack(fill="x", padx=20)

title_label = tk.Label(title_frame, 
                      text="🎮 Welcome to Hangman! 🎯",
                      font=("Segoe UI Variable Display", 24, "bold"),
                      bg="#EAB3B3",
                      fg="#640303")
title_label.pack(pady=10)


game_frame = tk.Frame(main_frame, bg="#EAB3B3")
game_frame.pack(pady=5)

# Canvas with decorative border
canvas_frame = tk.Frame(game_frame, bd=2, bg="#ffffff")
canvas_frame.pack(pady=5)

display_stickman = tk.Canvas(canvas_frame, 
                           width=200, 
                           height=200, 
                           bg="#ffffff",
                           highlightthickness=0)
display_stickman.pack(padx=5, pady=5)

# Game state variables
wrong_guesses = 0
display_word = tk.StringVar()
display_word.set("_ " * len(hangman_word))

# Word display frame
word_frame = tk.Frame(main_frame, bg="#EAB3B3")
word_frame.pack()

tk.Label(word_frame,
         text=f"Your Word: ({len(hangman_word)} letters)",
         font=("Helvetica", 12, "bold"),
         bg="#EAB3B3",
         fg="#640303").pack(pady=(5,0))

tk.Label(word_frame,
         textvariable=display_word,
         font=("Helvetica", 24, "bold"),
         bg="#EAB3B3").pack()

# Guessed letters tracking
guessed_letters = set()
guessed_display = tk.StringVar()
guessed_display.set("Guessed letters: ")

tk.Label(word_frame,
         textvariable=guessed_display,
         font=("Helvetica", 12),
         bg="#EAB3B3",
         fg="#640303").pack()

# Input frame
input_frame = tk.Frame(main_frame, bg="#EAB3B3")
input_frame.pack()

letter_entry = tk.Entry(input_frame, 
                       font=("Helvetica", 14), 
                       width=7,
                       justify="center")
letter_entry.pack(pady=10)


keyboard_section = tk.Frame(main_frame, bg="#EAB3B3", bd=2)
keyboard_section.pack(fill="x", padx=5)

tk.Label(keyboard_section,
         text="Virtual Keyboard",
         font=("Helvetica", 10, "bold"),
         bg="#EAB3B3",
         fg="#640303").pack(pady=2)

keyboard_frame = tk.Frame(keyboard_section, bg="#EAB3B3")
keyboard_frame.pack(pady=2)

keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]

def virtual_keyboard_press(letter):
    letter_entry.delete(0, tk.END)
    letter_entry.insert(0, letter)
    check_letter()

for row_idx, row in enumerate(keyboard_layout):
    row_frame = tk.Frame(keyboard_frame, bg="#EAB3B3")
    row_frame.pack(pady=2)
    
    if row_idx == 1:
        tk.Label(row_frame, width=1, bg="#EAB3B3").pack(side=tk.LEFT) 
    elif row_idx == 2:
        tk.Label(row_frame, width=2, bg="#EAB3B3").pack(side=tk.LEFT)

    for letter in row:
        button = tk.Button(row_frame, 
                          text=letter,
                          width=6,
                          height=2,
                          font=("Arial", 10, "bold"),
                          bg="#BE8484",
                          fg="#FFFFFF",
                          activebackground="#640303",
                          activeforeground="#FFFFFF",
                          cursor="hand2",
                          command=lambda l=letter: virtual_keyboard_press(l))
        button.pack(side=tk.LEFT, padx=1)

control_frame = tk.Frame(main_frame, bg="#EAB3B3")
control_frame.pack(pady=10, fill="x")

check_button = tk.Button(control_frame, 
                        text="Check Letter",
                        font=("Helvetica", 14, "bold"),
                        fg="#FDD8D8",
                        bg="#640303",
                        activebackground="#8B0000",
                        activeforeground="#FFFFFF",
                        cursor="hand2",
                        relief="raised",
                        command=check_letter)
check_button.pack(pady=10)


root.mainloop()

