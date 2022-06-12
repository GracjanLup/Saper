import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
from PIL import Image, ImageTk, ImageFilter

CZAS=0
LICZBAMIN=10
LICZBASZCZUROW=LICZBAMIN

def Witaj():
    # print("siema")
    emotikona.config(image=przyciskwow)
    emotikona.after(300, aktualizujEmotke)

def koniecgry_emotikona():
    emotikona.config(image=przyciskprzegrany)

def aktualizujEmotke():
    emotikona.config(image=emotikona_przycisk)

def Start():
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
    aktualizacjaLicznikaMin(licznik_min)
    panel_gorny=[zegar, licznik_min]
    return panel_gorny

def aktualizacjaZegara(root, zegar):
    global CZAS
    CZAS+=1
    zegar["text"]="0"*(3-len(str(CZAS)))+str(CZAS)
    root.after(1000, aktualizacjaZegara, root, zegar)

def aktualizacjaLicznikaMin(licznik_min):
    global LICZBAMIN
    for mina in range (LICZBAMIN, -1):
        print(mina)
# dałabym tutaj odniesienie do funkcji oflagowania, gdzie jest wstępna liczba flag-- poziom łatwy, średni, trudny
    licznik_min["text"]=LICZBAMIN

def zmiana_licznika_min(licznik_min):
    wartoscpoczatkowa=LICZBAMIN
    wartoscpooflagowaniu=LICZBAMIN-1
    licznik_min.config(wartośćpooflagowaniu)

def right_click(a):
    zmniejszanie_licznika_min=LICZBAMIN-1
    pola_gry[a].config(image=szczur, command='')
    pola_gry[a].bind('<Button-3>', lambda event: reset(a))


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

zegar = tk.Label(bg="black", fg="red", font=("Digital-7", 20))
zegar.place(x=190, y=10)
zegar["text"]="001"

szczur = Image.open("szczur.png")
szczur = szczur.resize((40,40))
szczur = ImageTk.PhotoImage(szczur)

licznik_min=tk.Label(root, bg="black", fg="red", font=("Digital-7", 20))
licznik_min.place(x=0, y=10)
licznik_min["text"]="001"
pola_gry=tk.Button(root, command=zmiana_licznika_min)

emotikona_przycisk=Image.open("buzka_usmiech.png")
emotikona_przycisk=emotikona_przycisk.resize((40,40))
emotikona_przycisk=ImageTk.PhotoImage(emotikona_przycisk)
emotikona=tk.Button(root, width=40, height=40, image=emotikona_przycisk, command=lambda:[Witaj()])
emotikona.place(x=97, y=0)

przyciskwow = Image.open("buzka_wow.png")
przyciskwow = przyciskwow.resize((30,30))
przyciskwow = ImageTk.PhotoImage(przyciskwow)

przyciskprzegrany=Image.open("buzka_smierc.png")
przyciskprzegrany=przyciskprzegrany.resize((30,30))
przyciskprzegrany=ImageTk.PhotoImage(przyciskprzegrany)
pola_gry = tk.Button(root, command=koniecgry_emotikona)

Start()
panel_gorny=PanelGorny(root)
root.mainloop()
