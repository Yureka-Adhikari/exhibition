from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(background="#EDC1BD")

choices = ["Rock", "Paper", "Scissors"]
result_label = Label(root, text="", font=("MS serif", 12), bg="#EDC1BD", fg="#460000")
result_label.place(x=50, y=240)

def computer_choice():
    return random.choice(choices)

score = 0
score_lbl = Label(root, text=f"Your score: {score}", font=("MS Serif", 12), bg="#EDC1BD", fg="#7D0000")
score_lbl.place(x=130, y=280)

def play(player_choice):
    global score
    comp_choice = computer_choice()
    
    if player_choice == comp_choice:
        result_label.config(text=f"It's a tie! Computer's choice was {comp_choice}")
        
    elif (player_choice == "Rock" and comp_choice == "Scissors") or \
         (player_choice == "Paper" and comp_choice == "Rock") or \
         (player_choice == "Scissors" and comp_choice == "Paper"):
        result_label.config(text=f"You win! Computer's choice was {comp_choice}")
        score += 1
        score_lbl.config(text=f"Your score: {score}") 

            
    else:
        result_label.config(text=f"You lose! Computer's choice was {comp_choice}")

def reset():
    result_label.config(text="")

rock = Button(root, text="Rock", bg="#7D0000", fg="white", command= lambda: play("Rock"))
paper = Button(root, text="Paper", bg="#7D0000", fg="white", command=lambda: play("Paper"))
scissors = Button(root, text="Scissors", bg="#7D0000", fg="white", command=lambda: play("Scissors"))

reset = Button(root, text="Reset", bg="#7D0000", fg="white", command=reset)
reset_score = Button(root, text="Reset Score", bg="#7D0000", fg="white", command=lambda: score_lbl.config(text="Your score: 0"))

rock_emj = Label(root, text="🪨", font=("Arial", 50), bg="#EDC1BD", borderwidth=1, relief="solid")
paper_emj = Label(root, text="📃", font=("Arial", 50), bg="#EDC1BD", borderwidth=1, relief="solid")
scissors_emj = Label(root, text="✂️", font=("times new roman", 50), bg="#EDC1BD", borderwidth=1, relief="solid")

rock.place(x=50, y=100)
paper.place(x=130, y=100)
scissors.place(x=210, y=100)
reset.place(x=50, y=280)
reset_score.place(x=50, y=310)

rock_emj.place(x=50, y=130)
paper_emj.place(x=130, y=130)
scissors_emj.place(x=210, y=130)

root.mainloop()