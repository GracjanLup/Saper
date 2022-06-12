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

    # difiniowanie przycisku do uruchomienia gry
    start_button = Button(root, text='Start!', font=button_font, command=lambda:[hide_all_widgets(), set_level_of_game()])
    start_button.pack()

##### Wybór poziomu trudności gry #####
def set_level_of_game():
    # definiowanie tekstu informacyjnego
    info = Label(text="Wybierz poziom trudności gry:", font=info_font)
    info.pack()

    ### Przyciski określające możliwe do wyboru poziomy gry ###
    # kliknięcie przycisku skutkuje uruchomieniem funkcji run_game z odpowiednimi parametrami
    # poziom łatwy
    l1 = Button(text='Latwy', font=button_font, command=lambda:[hide_all_widgets(), run_game(10, 8, 8, "easy")])
    l1.pack()

    # poziom średni
    l2 = Button(text='Trudny', font=button_font, command=lambda:[hide_all_widgets(), run_game(40, 16, 16, "hard")])
    l2.pack()

##### Uruchomienie gry #####
def run_game(number_of_mines, number_of_rows, number_of_columns, level_game):

    # definiowanie zmiennej globalnej przechowującej informacje o poziomie trudności gry
    global level
    level = level_game

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
    # generowanie przycisków dla poziomu łatwego
    if level == "easy":
        pola_gry = [tk.Button(main_panel, image=test, command=partial(check_position_easy, i)) for i in range(number_of_fields)]
    # generowanie przycisków dla poziomu trudnego
    else:
        pola_gry = [tk.Button(main_panel, image=test, command=partial(check_position_hard, i)) for i in range(number_of_fields)]

    # rysowanie planszy
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            pola_gry[i * number_of_columns + j].grid(row = j, column = i)
            pola_gry[i * number_of_columns + j].bind('<Button-3>', right_click)

##### Sprawdzanie pól dla poziomu łatwego - czy mina, sprawdzanie sąsiadów #####
def check_position_easy(i):
    # określenie krawędzi - pola wymagające szczególnego sprawdzenia
    left_edges = [x for x in range(1, 7)]
    bottom_edges = [x for x in range(15, 56, 8)]
    right_edges = [x for x in range(57, 63)]
    upper_udges = [x for x in range(8, 49, 8)]

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

        # funkcja przypisująca odpowiedni obrazek prezentujący cyfrę
        # zależność od ilości posiadanych bomb jako sąsiadów
        set_image_of_number(i, count)

##### Sprawdzanie pól dla poziomu trudnego - czy mina, sprawdzanie sąsiadów #####
def check_position_hard(i):
    # określenie krawędzi - pola wymagające szczególnego sprawdzenia
    left_edges = [x for x in range(1, 15)]
    bottom_edges = [x for x in range(31, 240, 16)]
    right_edges = [x for x in range(241, 255)]
    upper_udges = [x for x in range(16, 225, 16)]

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
            numbers = [i + 1, i + 16, i + 17]
            count = neighbour_check(numbers)
        # lewy dolny róg - ilość bomb jako sąsiadów
        elif i == 15:
            numbers = [i - 1, i + 15, i + 16]
            count = neighbour_check(numbers)
        # prawy górny róg - ilość bomb jako sąsiadów
        elif i == 240:
            numbers = [i - 16, i - 15, i + 1]
            count = neighbour_check(numbers)
        # prawy dolny róg - ilość bomb jako sąsiadów
        elif i == 255:
            numbers = [i - 17, i - 16, i - 1]
            count = neighbour_check(numbers)
        # lewa krawędź - ilość bomb jako sąsiadów
        elif i in left_edges:
            numbers = [i - 1, i + 1, i + 15, i + 16, i + 17]
            count = neighbour_check(numbers)
        # dolna krawędź - ilość bomb jako sąsiadów
        elif i in bottom_edges:
            numbers = [i - 17, i - 16, i - 1, i + 15, i + 16]
            count = neighbour_check(numbers)
        # prawa krawędź - ilość bomb jako sąsiadów
        elif i in right_edges:
            numbers = [i - 17, i - 16, i - 15, i - 1, i + 1]
            count = neighbour_check(numbers)
        # górna krawędź - ilość bomb jako sąsiadów
        elif i in upper_udges:
            numbers = [i - 16, i - 15, i + 1, i + 16, i + 17]
            count = neighbour_check(numbers)
        # pozostałe pola - ilość bomb jako sąsiadów
        else:
            numbers = [i - 17, i - 16, i - 15, i - 1, i + 1, i + 15, i + 16, i + 17]
            count = neighbour_check(numbers)

        # funkcja przypisująca odpowiedni obrazek prezentujący cyfrę
        # zależność od ilości posiadanych bomb jako sąsiadów
        set_image_of_number(i, count)

##### Przypisywanie obrazka prezentującego cyfrę - zależność od posiadanych bomb sąsiadów #####
def set_image_of_number(i, count):
    # liczba bomb 1 - przypisz obrazek cyfra1
    if count == 1:
        pola_gry[i].config(image=cyfra1)
    # analogicznie jak wyżej
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
        pola_gry[i].unbind('<Button-3>')
    for j in mines_positions:
        pola_gry[j].config(image=mina)

##### Prawe kliknięcie myszy #####
def right_click(event):
    # usunięcie możliwości sprawdzenia pozycji przy ustawionej fladze
    event.widget.configure(image = flaga, command = '')
    # zbindowanie na prawym przycisku funkcji reset
    event.widget.bind('<Button-3>', reset)

##### Ponowne kliknięcie prawego przycisku myszy - usunięcie flagi #####
def reset(event):
    # sprawdzene indeksu dla klikniętego widgetu w liście
    index_of_button = pola_gry.index(event.widget)
    # w zależności od levelu przypisujemy na nowo obrazek i wywoływaną funkcję po kliknięciu
    if level == "easy":
        event.widget.configure(image = test, command = partial(check_position_easy, index_of_button))
    else:
        event.widget.configure(image=test, command=partial(check_position_hard, index_of_button))
    # zbindowanie na prawym przycisku funkcji right_click
    event.widget.bind('<Button-3>', right_click)

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
