import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "Ini adalah pesan info!")

root = tk.Tk()
root.title("Contoh Messagebox")

button = tk.Button(root, text="Tampilkan Pesan", command=show_message)
button.pack(pady=20)

root.mainloop()