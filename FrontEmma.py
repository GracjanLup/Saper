
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
from PIL import Image, ImageTk
CZAS=0

def Start():
    print("siema")
    PanelGlowny(root)

def PanelGlowny(root):
    przyciski = [tk.Button(frame, width = 2, height = 1) for i in range(Kolumny*Wiersze)]
    pola_gry = [tk.Button(frame, width = 2, height = 1) for i in range(Kolumny*Wiersze)]

    for i in range(Wiersze):
        for j in range(Kolumny):
            pola_gry[i*Kolumny + j].grid(row = i+1, column = j)
    return pola_gry

def PanelGorny(root):

    aktualizacjaZegara(root, zegar)

    # licznik_min=tk.Label(root, bg="black", fg="red", font=("Digital-7", 20))
    # licznik_min.place(x=200, y=10)
    # licznik_min["text"]="000"
    # aktualizacjaLicznikaMin(root, licznik_min)



    panel_gorny=[zegar, emotikona]
    return panel_gorny

def aktualizacjaZegara(root, zegar):
    global CZAS
    CZAS+=1
    zegar["text"]="0"*(3-len(str(CZAS)))+str(CZAS)
    root.after(1000, aktualizacjaZegara, root, zegar)

# def aktualizacjaLicznikaMin()
Kolumny = 10
Wiersze = 10
root = tk.Tk()
root.title('Saper')
root.geometry('600x400')
InfoFont = font.Font(family='Tahoma', size=20)
ButtonFont = font.Font(family='Tahoma', size=20)
panel_gorny = tk.Frame(root, bg="pink")
panel_gorny.place(relwidth=1, relheight=0.125)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=0.875, rely=0.125)

zegar= tk.Label(bg="black", fg="red", font=("Digital-7", 20))
zegar.place(x=370, y=10)
zegar["text"]="0001"

emotikona_przycisk=Image.open("buzka_usmiech.png")
emotikona_przycisk=emotikona_przycisk.resize((60,60))
emotikona_przycisk=ImageTk.PhotoImage(emotikona_przycisk)
emotikona=tk.Button(root, width=20, height=20, image=emotikona_przycisk)
emotikona.place(x=290, y=10)


Start()
panel_gorny=PanelGorny(root)
root.mainloop()
