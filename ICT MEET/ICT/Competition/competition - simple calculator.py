import tkinter as tk

def update_display(value):
    currentvalue = Display_var.get()
    if value == "0":
        Display_var.set(currentvalue)
    else:
        Display_var.set(currentvalue + value)
    
def clear_display():
    Display_var.set(" ")
    
def calculate_result():
    try:
        res = eval(Display_var.get())
        Display_var.set(str(res))
    except:
        Display_var.set("Error")

        
parent = tk.Tk()
parent.title("Simple Calculator")
parent.configure(bg="#ffedba")

frame = tk.Frame(parent, background="#f7d9c6", bd=10, relief="ridge")
frame.grid(row=0, column=5, padx=20, pady=20)

Display_var = tk.StringVar()
Display_var.set(" ")

tk.Label(frame, text="🧮Calculator📐", font=("Segoe Script", 19),fg="#3a1800",background="#f7d9c6").grid(row=0, column=3, columnspan=4, pady=10)

button_frame = tk.Frame(frame, bg="#e4d6a7", border=10, relief="ridge", height =800, width = 800)
button_frame.grid(row=1, column=3, pady=10, padx=20)

display = tk.Label(button_frame, textvariable=Display_var, font=("Arial", 24), bg="#faf5db", width=15, border=2, height = 2)
display.grid(row=0, column=0, columnspan=4,pady=0)

button_layout = [
                 ("%", 1, 0,), ("//",1,1),("**",1,2),("sqrt",1,3),
                 ("7", 2, 0),("8", 2, 1),("9", 2, 2),("/", 2, 3),
                 ("4", 3, 0),("5", 3, 1),("6", 3, 2),("*", 3, 3),
                 ("1", 4, 0),("2", 4, 1),("3", 4, 2),("-", 4, 3),
                 (".", 5, 0),("0", 5, 1),("+", 5, 2),("=", 5, 3),
                ]

for (text,row,col) in button_layout:
    if text == "sqrt":
        button = tk.Button(button_frame, text= text, padx=20, height=2, width =2, font=("Arial", 18), background="#e2ce9f",border=1, borderwidth=1,
command=lambda: update_display("**0.5"))
        button.grid(row=row, column=col)
    elif text =="=":
        button = tk.Button(button_frame, text= text, padx=20, height=2, width =2, font=("Arial", 18), background="#ebc1c1",border=1, borderwidth=1,
command=calculate_result)
        button.grid(row=row, column=col)
    else:
        button = tk.Button(button_frame, text= text, padx=20, height=2, width =2, font=("Arial", 18), background="#e2ce9f",border=1, borderwidth=1,
command=lambda val=text: update_display(val))
        button.grid(row=row, column=col)
        
clear_btn = tk.Button(button_frame, text= "C", padx=20, height=2, width =2, font=("Arial", 18), background="#e2ce9f",border=1, borderwidth=1, command=clear_display)
clear_btn.grid(row=6, column=0, columnspan=4)

def delete_last():
    txt = Display_var.get()
    if txt in ("0", "Error"):
        Display_var.set("0")
        return
    txt = txt[:-1]
    Display_var.set(txt if txt else "0")


def handle_key(event):

    ch = event.char
    ks = event.keysym

    if ch in '0123456789.+-*/':
        if Display_var.get() in ("0", "Error"):
            Display_var.set(ch)
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

parent.bind('<Key>', handle_key)

parent.mainloop()
