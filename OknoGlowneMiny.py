import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter

# Pamiętajcie o:
# "pip install Pillow" w cmd'ku

def Start():
    print("siema")
    Panel_glowny(root)

def Panel_glowny(root):
    pola_gry = [tk.Button(frame, width = 30, height = 30, image=test) for i in range(Kolumny*Wiersze)]
    for i in range(Wiersze):
        for j in range(Kolumny):
            pola_gry[i*Kolumny + j].grid(row = i+1, column = j)
    return pola_gry

def Prawy_przycisk():
    pola_gry[x,y].config(image="Grafika/flaga.png")

def Lewy_przycisk():
    print("Ok")

def Wylosowanie_min():
    liczba_min = 20
    pozycje_min = []
    for i in range(liczba_min):
        tmp = [random.randint(1,10), random.randint(1,10)]
        while tmp in pozycje_min:
            tmp = [random.randint(1,10), random.randint(1,10)]
        pozycje_min.append(tmp)
    return pozycje_min

Kolumny = 10
Wiersze = 10

root = tk.Tk()
root.title('Saper')
root.geometry('350x400')

obraz = Image.open("Grafiki/test.png")
obraz = obraz.resize((30, 30))
obraz = obraz.filter(ImageFilter.CONTOUR)
test = ImageTk.PhotoImage(obraz)

InfoFont = font.Font(family='Tahoma', size=20)
ButtonFont = font.Font(family='Tahoma', size=20)

panel_gorny = tk.Frame(root, bg="pink")
panel_gorny.place(relwidth=1, relheight=0.125)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=0.875, rely=0.125)

StartButton = Button(root, text="Start", padx=10, pady=5, font=ButtonFont, command=lambda:[StartButton.pack_forget(), Start()])
StartButton.pack()

root.mainloop()
