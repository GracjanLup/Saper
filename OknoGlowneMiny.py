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

##### Panel powitalny #####
def welcome_panel():
    # definiowanie tekstu powitalnego
    welcome = Label(root, text="Witamy w grze Saper!", font=info_font)
    welcome.pack()

    # difiniowanie przycisku do uruchmienia gry
    start_button = Button(root, text='Start!', font=button_font, command=lambda:[hide_all_widgets(), set_level_of_game()])
    start_button.pack()

##### Wybór poziomu trudności gry #####
def set_level_of_game():
    # definiowanie tekstu informacyjnego
    info = Label(text="Wybierz poziom trudności gry:", font=info_font)
    info.pack()

    ### Przyciski określające możliwe do wyboru poziomy gry ###
    # kliknięcie przycisku skutkuje uruchomieniem funkcji run_game
    # poziom łatwy
    l1 = Button(text='Latwy', font=button_font, command=lambda:[hide_all_widgets(), run_game(10, 8, 8)])
    l1.pack()

    # poziom średni
    l2 = Button(text='Sredni', font=button_font, command=lambda:[hide_all_widgets(), run_game(40, 16, 16)])
    l2.pack()

    # poziom trudny
    l3 = Button(text='Trudny', font=button_font, command=lambda:[hide_all_widgets(), run_game(99, 30, 16)])
    l3.pack()

##### Uruchomienie gry #####
def run_game(number_of_mines, number_of_rows, number_of_columns):
    # definiowanie łącznej ilości pól
    number_of_fields = number_of_rows * number_of_columns

    # definicja zmiennej globalnej przechowującej pozycje min
    global mines_positions
    # wywołanie funkcji losującej pozycje min, przypisanie do zmiennej globalnej
    mines_positions = draw_of_mines(number_of_mines, number_of_fields)

    # definiowanie wyglądu - panel górny
    upper_panel = tk.Frame(root, bg="grey")
    upper_panel.place(relwidth=1, relheight=0.125)

    # definiowanie wyglądu - panel dolny
    main_panel = tk.Frame(root, bg="white")
    main_panel.place(rely=0.5, relx=0.5, anchor=CENTER)

    # definicja zmiennej globalnej przechowującej pola gry
    global pola_gry
    # przyciski posiadają unikalne identyfikatory
    # partial pozwala na uruchomienie funkcji z parametrem - w tym przypadku sprawdzającej właściwości pola
    pola_gry = [tk.Button(main_panel, image=test, command=partial(check_position, i)) for i in range(number_of_fields)]

    # rysowanie planszy
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            pola_gry[i * number_of_columns + j].grid(row = j, column = i)

    pola_gry[0].bind('<Button-3>', lambda event: right_click(0))
    pola_gry[1].bind('<Button-3>', lambda event: right_click(1))
    pola_gry[2].bind('<Button-3>', lambda event: right_click(2))
    pola_gry[3].bind('<Button-3>', lambda event: right_click(3))
    pola_gry[4].bind('<Button-3>', lambda event: right_click(4))
    pola_gry[5].bind('<Button-3>', lambda event: right_click(5))
    pola_gry[6].bind('<Button-3>', lambda event: right_click(6))
    pola_gry[7].bind('<Button-3>', lambda event: right_click(7))
    pola_gry[8].bind('<Button-3>', lambda event: right_click(8))
    pola_gry[9].bind('<Button-3>', lambda event: right_click(9))
    pola_gry[10].bind('<Button-3>', lambda event: right_click(10))
    pola_gry[11].bind('<Button-3>', lambda event: right_click(11))
    pola_gry[12].bind('<Button-3>', lambda event: right_click(12))
    pola_gry[13].bind('<Button-3>', lambda event: right_click(13))
    pola_gry[14].bind('<Button-3>', lambda event: right_click(14))

##### Sprawdzanie pola - czy mina, sprawdzanie sąsiadów #####
def check_position(i):
    # określenie krawędzi - pola wymagające szczególnego sprawdzenia
    left_edges = [1, 2, 3, 4, 5, 6]
    bottom_edges = [15, 23, 31, 39, 47, 55]
    right_edges = [57, 58, 59, 60, 61, 62]
    upper_udges = [8, 16, 24, 32, 40, 48]

    # definicja liczby określającej ilośc
    count = 0

    # sprawdzenie czy pozycja jest miną:
    # TAK - koniec gry
    # NIE - sprawdzanie ilości bomb jako sąsiadów
    if i in mines_positions:
        pola_gry[i].config(image=mina_red)
        end_game(i)
    else:
        # lewy górny róg - ilość bomb jako sąsiadów
        if i == 0:
            numbers = [i + 1, i + 8, i + 9]
            count = neighbour_check(numbers)
        # lewy dolny róg - ilość bomb jako sąsiadów
        elif i == 7:
            numbers = [i - 1, i + 7, i + 8]
            count = neighbour_check(numbers)
        # prawy górny róg - ilość bomb jako sąsiadów
        elif i == 56:
            numbers = [i - 8, i - 7, i + 1]
            count = neighbour_check(numbers)
        # prawy dolny róg - ilość bomb jako sąsiadów
        elif i == 63:
            numbers = [i - 9, i - 8, i - 1]
            count = neighbour_check(numbers)
        # lewa krawędź - ilość bomb jako sąsiadów
        elif i in left_edges:
            numbers = [i - 1, i + 1, i + 7, i + 8, i + 9]
            count = neighbour_check(numbers)
        # dolna krawędź - ilość bomb jako sąsiadów
        elif i in bottom_edges:
            numbers = [i - 9, i - 8, i - 1, i + 7, i + 8]
            count = neighbour_check(numbers)
        # prawa krawędź - ilość bomb jako sąsiadów
        elif i in right_edges:
            numbers = [i - 9, i - 8, i - 7, i - 1, i + 1]
            count = neighbour_check(numbers)
        # górna krawędź - ilość bomb jako sąsiadów
        elif i in upper_udges:
            numbers = [i - 8, i - 7, i + 1, i + 8, i + 9]
            count = neighbour_check(numbers)
        # pozostałe pola - ilość bomb jako sąsiadów
        else:
            numbers = [i - 9, i - 8, i - 7, i - 1, i + 1, i + 7, i + 8, i + 9]
            count = neighbour_check(numbers)

        # przypisanie odpowiedniego obrazka prezentującego cyfrę
        # zależność od ilości posiadanych bomb jako sąsiadów
        if count == 1:
            pola_gry[i].config(image=cyfra1)
        elif count == 2:
            pola_gry[i].config(image=cyfra2)
        elif count == 3:
            pola_gry[i].config(image=cyfra3)
        elif count == 4:
            pola_gry[i].config(image=cyfra4)
        elif count == 5:
            pola_gry[i].config(image=cyfra5)
        elif count == 0:
            pola_gry[i].config(image=cyfra0)

##### Sprawdzanie ilości bomb jako sąsiadów #####
def neighbour_check(numbers):
    count = 0
    for x in numbers:
        if x in mines_positions:
            count += 1
    return count

##### Generowanie unikalnych pozycji min #####
def draw_of_mines(number_of_mines, number_of_fields):
    mines_positions = []
    for i in range(number_of_mines):
        tmp = random.randint(0, number_of_fields)
        while tmp in mines_positions:
            tmp = random.randint(0, number_of_fields)
        mines_positions.append(tmp)
    print(mines_positions)
    return mines_positions

##### Ukrywanie wszystkich aktualnie wyświetlanych widgetów #####
def hide_all_widgets():
    for widgets in root.winfo_children():
        widgets.destroy()

##### Koniec gry #####
def end_game(i):
    print("Przegrałeś")
    mines_positions.remove(i)
    for i in range(len(pola_gry)):
        pola_gry[i].config(command='')
    for j in mines_positions:
        pola_gry[j].config(image=mina)

##### Prawe kliknięcie myszy #####
def right_click(a):
    pola_gry[a].config(image=flaga, command='')
    pola_gry[a].bind('<Button-3>', lambda event: reset(a))

##### Ponowne kliknięcie prawego przycisku myszy #####
def reset(a):
    pola_gry[a].config(image=test, command=partial(check_position, a))
    pola_gry[a].bind('<Button-3>', lambda event: right_click(a))

root = tk.Tk()
root.title('Saper')
root.geometry('1200x800')

obraz = Image.open("Grafiki/test.png")
obraz = obraz.resize((40,40))
test = ImageTk.PhotoImage(obraz)

# inicjalizacja grafiki dla bomby
mina = Image.open("Grafiki/bomba.png")
mina = mina.resize((40,40))
mina = ImageTk.PhotoImage(mina)

mina_red = Image.open("Grafiki/bomba_red.png")
mina_red = mina_red.resize((40,40))
mina_red = ImageTk.PhotoImage(mina_red)

# inicjalizacja grafiki dla flagi
flaga = Image.open("Grafiki/flaga.png")
flaga = flaga.resize((40,40))
flaga = ImageTk.PhotoImage(flaga)

# inicjalizacja grafik liczb
cyfra1 = Image.open("Grafiki/1.png")
cyfra1 = cyfra1.resize((40,40))
cyfra1 = ImageTk.PhotoImage(cyfra1)

cyfra2 = Image.open("Grafiki/2.png")
cyfra2 = cyfra2.resize((40,40))
cyfra2 = ImageTk.PhotoImage(cyfra2)

cyfra3 = Image.open("Grafiki/3.png")
cyfra3 = cyfra3.resize((40,40))
cyfra3 = ImageTk.PhotoImage(cyfra3)

cyfra4 = Image.open("Grafiki/4.png")
cyfra4 = cyfra4.resize((40,40))
cyfra4 = ImageTk.PhotoImage(cyfra4)

cyfra5 = Image.open("Grafiki/5.png")
cyfra5 = cyfra5.resize((40,40))
cyfra5 = ImageTk.PhotoImage(cyfra5)

cyfra0 = Image.open("Grafiki/0.png")
cyfra0 = cyfra0.resize((40,40))
cyfra0 = ImageTk.PhotoImage(cyfra0)

info_font = font.Font(family='Tahoma', size=20)
button_font = font.Font(family='Tahoma', size=20)

##### Uruchomienie wykonywania programu #####
welcome_panel()

root.mainloop()
