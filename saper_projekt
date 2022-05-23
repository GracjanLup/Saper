import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time

def start1():
    print("Ok")

root = tk.Tk()
root.title('Badanie rozwiązywania problemów')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

InfoFont = font.Font(family='Tahoma', size=20)
ButtonFont = font.Font(family='Tahoma', size=25)

canvas = tk.Canvas(root, bg="#d9d1e0")
canvas.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.6, relheight=0.6, relx=0.2, rely=0.2)

info1 = Label(canvas, text="Badanie trzecie: rozwiązywania problemów", pady=20, font=InfoFont, bg="#d9d1e0")
info1.pack()

info2 = Label(frame, text="Po ", pady=20, font=InfoFont, bg="white", wraplength=700, justify="center")
info2.pack()

StartButton = Button(canvas, text="Zacznij badanie", padx=10, pady=5, font=ButtonFont, command=lambda:[StartButton.pack_forget(), start1()])
StartButton.pack()

root.mainloop()
