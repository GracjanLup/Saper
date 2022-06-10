import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter
from functools import partial

# Pamiętajcie o:
# "pip install Pillow" w cmd'ku

# panel powitalny
def welcome_panel():
    welcome = Label(root, text="Witamy w grze Saper!", font=info_font)
    welcome.pack()

    startButton = Button(root, text='Start!', font=button_font, command=lambda:[hide_all_widgets(), set_level_of_game()])
    startButton.pack()

# panel wyboru poziomu trudności gry
def set_level_of_game():
    info = Label(text="Wybierz poziom trudności gry:", font=info_font)
    info.pack()

    # kliknięcie w przycisk ukrywa wszystkie wyświetlone widgety
    # oraz wywołuje funkcję run_game
    l1 = Button(text='Latwy', font=button_font, command=lambda:[hide_all_widgets(), run_game(10, 8, 8)])
    l1.pack()

    l2 = Button(text='Sredni', font=button_font, command=lambda:[hide_all_widgets(), run_game(40, 16, 16)])
    l2.pack()

    l3 = Button(text='Trudny', font=button_font, command=lambda:[hide_all_widgets(), run_game(99, 30, 16)])
    l3.pack()

# uruchomienie gry
def run_game(number_of_mines, number_of_rows, number_of_columns):
    # zdefiniowanie liczby pól
    number_of_fields = number_of_rows * number_of_columns

    # zmienna globalna z przypisanymi wylosowanymi pozycjami min
    global mines_positions
    mines_positions = draw_of_mines(number_of_mines, number_of_fields)

    # ustalenie górnego panelu
    upper_panel = tk.Frame(root, bg="grey")
    upper_panel.place(relwidth=1, relheight=0.125)

    # ustalenie dolnego panelu
    # wyśrodkowanie
    main_panel = tk.Frame(root, bg="white")
    main_panel.place(rely=0.5, relx=0.5, anchor=CENTER)

    # zmienna globalna z polami gry
    # każdy przycisk posiada swój unikalny identyfikator
    # partial w command służy do uruchamiania funkcji ze wskazanym parametrem
    global pola_gry
    pola_gry = [tk.Button(main_panel, image=test, command=partial(check_position, i)) for i in range(number_of_columns*number_of_rows)]
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            pola_gry[i * number_of_columns + j].grid(row = j, column = i)

# sprawdzenie pozycji po kliknięciu - czy bomba czy wyświetlić liczbę
# do dokończenia sprawdzanie sąsiadów w przypadku, gdy kliknięty przycisk jest przy krawędzi
# oraz pojawianie się pól, gdy wartość jest równa 0
def check_position(i):
    count = 0
    print(i)
    if i in mines_positions:
        pola_gry[i].config(image=mina)
    else:
        numbers = [i - 9, i - 8, i - 7, i - 1, i + 1, i + 7, i + 8, i + 9]
        print(i)
        for x in numbers:
            if x in mines_positions:
                count += 1
        pola_gry[i].config(image='', text=count)
    # do dokończenia sprawdzanie sąsiadów

# generowanie pozycji min
def draw_of_mines(number_of_mines, number_of_fields):
    mines_positions = []
    for i in range(number_of_mines):
        tmp = random.randint(0, number_of_fields)
        while tmp in mines_positions:
            tmp = random.randint(0, number_of_fields)
        mines_positions.append(tmp)
    print(mines_positions)
    return mines_positions

# ukrywanie wszystkich aktualnie wyświetlanych widgetów
def hide_all_widgets():
    for widgets in root.winfo_children():
        widgets.destroy()

root = tk.Tk()
root.title('Saper')
root.geometry('1200x800')

obraz = Image.open("Grafiki/test.png")
obraz = obraz.resize((30, 30))
test = ImageTk.PhotoImage(obraz)

# inicjalizacja grafiki dla bomby
mina = Image.open("Grafiki/bomba.png")
mina = mina.resize((30,30))
mina = ImageTk.PhotoImage(mina)

info_font = font.Font(family='Tahoma', size=20)
button_font = font.Font(family='Tahoma', size=20)



# uruchomienie wykonywania programu
welcome_panel()

root.mainloop()
