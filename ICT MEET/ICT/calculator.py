import tkinter as tk

def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

def clear_display():
    display_var.set("0")
    
def calculate_result():
    try:
        res = eval(display_var.get())
        display_var.set(str(res))
    except:
        display_var.set("Error")

parent = tk.Tk()
parent.title("Calculator")
parent.geometry('500x800')
parent.configure(bg="#e4d6a7")

frame = tk.Frame(parent, background="#e9cab6", bd=10, relief="ridge")
frame.pack(expand=True, padx=30, pady=30, fill=tk.BOTH)

display_var = tk.StringVar()
display_var.set("0")

tk.Label(frame, text="🧮Calculator📐", font=("Segoe Script", 19),fg="#3a1800",background="#e9cab6").grid(row=0, column=3, columnspan=4, pady=10)

button_frame = tk.Frame(frame, bg="#e4d6a7", border=10, relief="ridge", height = 400, width = 400)
button_frame.grid(row=1, column=3, columnspan=4, pady=10, padx=450)

display_label = tk.Label(button_frame, textvariable= display_var, padx=20, pady=20, font=("Arial", 18), anchor="e", bg="#ffffff")
display_label.grid(row=0, column=0, columnspan=4, sticky="we")

button_layout = [
    ("7",1,0), ("8",1,1), ("9", 1, 2), ("/", 1, 3),
    ("4",2,0), ("5",2,1), ("6", 2, 2), ("*", 2, 3),
    ("1",3,0), ("2",3,1), ("3", 3, 2), ("+", 3, 3),
    ("0",4,0), (".",4,1), ("=", 4,2), ("-", 4, 3)
]

for (text, row, col) in button_layout:
    button = tk.Button(button_frame, text= text, padx=20, pady=20, height=2, width =2, font=("Arial", 18), background="#e2ce9f",border=1, borderwidth=1,
command=lambda t=text: update_display(t) if t != "=" else calculate_result())
    button.grid(row=row, column=col)


clear_button = tk.Button(button_frame, text="AC", padx=20, pady=20, font=("Arial", 18),background="#e2ce9f", command = clear_display)
clear_button.grid(row=5, column=0, columnspan=4)

def delete_last():
    txt = display_var.get()
    if txt in ("0", "Error"):
        display_var.set("0")
        return
    txt = txt[:-1]
    display_var.set(txt if txt else "0")


def handle_key(event):

    ch = event.char
    ks = event.keysym

    if ch and ch in '0123456789.+-*/':
        if display_var.get() in ("0", "Error"):
            display_var.set(ch)
        else:
            update_display(ch)
        return

    if ch == '=':
        calculate_result()
        return

    if ks in ('Return', 'KP_Enter'):
        calculate_result()
        return
    
    if ks == 'BackSpace':
        delete_last()
        return


    if ks == 'Escape' or (ch and ch.lower() == 'c'):
        clear_display()
        return



parent.bind('<Key>', handle_key)
parent.focus_set()

parent.mainloop()
