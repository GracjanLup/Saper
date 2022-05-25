import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time

def Start():
    print("siema")
    PanelGlowny(root)

def PanelGlowny(root):
<<<<<<< Updated upstream
    przyciski = [tk.Button(frame, width = 2, height = 1) for i in range(Kolumny*Wiersze)]
=======
    pola_gry = [tk.Button(frame, width = 2, height = 1) for i in range(Kolumny*Wiersze)]
>>>>>>> Stashed changes

    for i in range(Wiersze):
        for j in range(Kolumny):
            pola_gry[i*Kolumny + j].grid(row = i+1, column = j)
    return pola_gry

Kolumny = 10
Wiersze = 10

root = tk.Tk()
root.title('Saper')
root.geometry('600x400')

InfoFont = font.Font(family='Tahoma', size=20)
ButtonFont = font.Font(family='Tahoma', size=20)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.4, relheight=0.66, relx=0.3, rely=0.17)

StartButton = Button(root, text="Start", padx=10, pady=5, font=ButtonFont, command=lambda:[StartButton.pack_forget(), Start()])
StartButton.pack()

root.mainloop()
