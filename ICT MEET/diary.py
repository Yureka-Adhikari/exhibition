import tkinter as tk
from tkinter import messagebox, simpledialog 
import os

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
            base_filename = filename
            while os.path.exists(filename):
                filename = f"diary_entries/{safe_title}_{count}.txt"
                count += 1
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", f"Diary entry '{title}' saved!")

        
def show_entries():
    create_directory()
    entries = os.listdir('diary_entries')
    if not entries:
        messagebox.showinfo("No Entries", "No diary entries found.")
        return
    
    entries_window = tk.Toplevel(root)
    entries_window.title("Diary Entries")
    entries_window.geometry("400x300")

    listbox = tk.Listbox(entries_window, width=50)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)
    
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
            text = tk.Text(content_window, width=50, height=15)
            text.pack()
            text.insert(tk.END, content)
            text.config(state=tk.DISABLED)
            
    listbox.bind('<<ListboxSelect>>', display_entry)

root = tk.Tk()
root.title('Diary')
root.geometry('400x400')

frame = tk.Frame(root)
frame.pack(expand=True)

text_entry = tk.Text(frame, height=15, width=40)
text_entry.pack(pady=20)

save_button = tk.Button(frame, text='Save', command=save_entry)
save_button.pack(pady=5)

show_button = tk.Button(frame, text='Show Entries', command=show_entries)
show_button.pack(pady=5)

quit_button = tk.Button(frame, text='Quit', command=root.quit)
quit_button.pack(pady=5)

root.mainloop()