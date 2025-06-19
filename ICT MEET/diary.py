import tkinter as tk
from tkinter import messagebox, simpledialog
import os

PASSWORD = "mysecret"

def check_password():
    pwd = simpledialog.askstring("Password", "Enter your diary password:", show="*")
    if pwd != PASSWORD:
        messagebox.showerror("Access Denied", "Incorrect password!")
        root.destroy()

def create_directory():
    if not os.path.exists('diary_entries'):
        os.makedirs('diary_entries')

def save_entry():
    create_directory()
    content = text_entry.get("1.0", tk.END).strip()
    if content:
        title = simpledialog.askstring("Entry Title", "Enter a title for your diary entry:")
        if title:
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_', '-')).rstrip()
            filename = f"diary_entries/{safe_title}.txt"
            count = 1
            while os.path.exists(filename):
                filename = f"diary_entries/{safe_title}_{count}.txt"
                count += 1
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", f"Diary entry '{title}' saved!")
            text_entry.delete("1.0", tk.END)

def show_entries():
    create_directory()
    entries = os.listdir('diary_entries')
    if not entries:
        messagebox.showinfo("No Entries", "No diary entries found.")
        return

    entries_window = tk.Toplevel(root)
    entries_window.title("Diary Entries")
    entries_window.geometry("450x350")
    entries_window.configure(bg="#e6e6fa")

    listbox = tk.Listbox(entries_window, width=40, font=("Segoe Script", 12), bg="#f3eaff", fg="#6d4c41", bd=2, relief="groove")
    listbox.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

    for entry in sorted(entries):
        listbox.insert(tk.END, entry)

    def display_entry(event):
        selection = listbox.curselection()
        if selection:
            filename = listbox.get(selection[0])
            with open(os.path.join('diary_entries', filename), "r", encoding="utf-8") as f:
                content = f.read()
            content_window = tk.Toplevel(entries_window)
            content_window.title(filename)
            content_window.configure(bg="#e6e6fa")
            frame = tk.Frame(content_window, bg="#e6e6fa", bd=5, relief="ridge")
            frame.pack(padx=20, pady=20)
            label = tk.Label(frame, text=filename, font=("Segoe Script", 14, "bold"), bg="#e6e6fa", fg="#7c5e99")
            label.pack(pady=(0,10))
            text = tk.Text(frame, width=40, height=12, font=("Segoe Script", 11), bg="#f3eaff", fg="#6d4c41", bd=2, relief="groove", wrap="word")
            text.pack()
            text.insert(tk.END, content)
            text.config(state=tk.DISABLED)

    listbox.bind('<<ListboxSelect>>', display_entry)

root = tk.Tk()
root.withdraw()
check_password()
root.deiconify()
root.title('My Scrapbook Diary')
root.geometry('500x650')
root.configure(bg="#e6e6fa")

frame = tk.Frame(root, bg="#d6c6f5", bd=10, relief="ridge")
frame.pack(expand=True, padx=30, pady=30, fill=tk.BOTH)

title_label = tk.Label(frame, text="📔 My Scrapbook Diary 📔", font=("Segoe Script", 20, "bold"), bg="#d6c6f5", fg="#7c5e99")
title_label.pack(pady=(10, 20))

text_entry = tk.Text(frame, height=15, width=45, font=("Segoe Script", 12), bg="#f3eaff", fg="#6d4c41", bd=3, relief="groove", wrap="word")
text_entry.pack(pady=10)

button_frame = tk.Frame(frame, bg="#d6c6f5")
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text='💾 Save', font=("Segoe Script", 12, "bold"), bg="#7c5e99", fg="#f3eaff", width=10, command=save_entry, bd=2, relief="raised", activebackground="#bfa2e6")
save_button.grid(row=0, column=0, padx=10)

show_button = tk.Button(button_frame, text='📖 Show Entries', font=("Segoe Script", 12, "bold"), bg="#7c5e99", fg="#f3eaff", width=15, command=show_entries, bd=2, relief="raised", activebackground="#bfa2e6")
show_button.grid(row=0, column=1, padx=10)

quit_button = tk.Button(frame, text='❌ Quit', font=("Segoe Script", 12, "bold"), bg="#7c5e99", fg="#f3eaff", width=10, command=root.quit, bd=2, relief="raised", activebackground="#bfa2e6")
quit_button.pack(pady=20, anchor="center")

tape1 = tk.Label(root, text="🩷", font=("Arial", 24), bg="#e6e6fa")
tape1.place(x=40, y=20)
tape2 = tk.Label(root, text="💜", font=("Arial", 24), bg="#e6e6fa")
tape2.place(x=420, y=20)

root.mainloop()