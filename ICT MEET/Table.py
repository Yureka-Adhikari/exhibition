from tkinter import Tk, Button, Frame
import subprocess

def open_order():
    subprocess.run(["python", "order.py"])

app = Tk()
app.title("Table Order Application")
app.geometry("300x400")
app.configure(bg="#F5F7FA")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

for i in range(10):
    row = i // 2
    col = i % 2
    frame = Frame(
        app,
        bg="#29005C",
        highlightthickness=0,
        bd=0
    )
    frame.grid(row=row, column=col, padx=25, pady=20, sticky="nsew")
    button = Button(
        frame,
        text=f"Table {i+1}",
        width=15,
        height=2,
        command=open_order,
        bg="#C8C6EA",
        activebackground="#CCCAF3",
        fg="#29005C",
        bd=0,
        highlightthickness=0
    )
    button.pack(padx=2, pady=2)

app.mainloop()