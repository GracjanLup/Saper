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

    zegar = tk.Label(bg="black", fg="red", font=("Digital-7", 20))
    zegar.place(x=190, y=10)
    zegar["text"]="001"

    licznik_min = tk.Label(root, bg="black", fg="red", font=("Digital-7", 20))
    licznik_min.place(x=0, y=10)
    licznik_min["text"]="001"

    # pola_gry=tk.Button(root, command=zmiana_licznika_min)

    # gorny_start()

    # definiowanie wyglądu - panel dolny
    main_panel = tk.Frame(root, bg="white")
    main_panel.place(relwidth=1, relheight=0.874, rely=0.125)

    # definicja zmiennej globalnej przechowującej pola gry
    global pola_gry
    # przyciski posiadają unikalne identyfikatory
    # partial pozwala na uruchomienie funkcji z parametrem - w tym przypadku sprawdzającej właściwości pola
    pola_gry = [tk.Button(main_panel, image=test, command=partial(check_position, i)) for i in range(number_of_fields)]

    # rysowanie planszy
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            pola_gry[i * number_of_columns + j].grid(row = j, column = i)

    for j in range(number_of_columns*number_of_rows):
        pola_gry[j].bind('<Button-3>', lambda event: right_click(j))

    # pola_gry[0].bind('<Button-3>', lambda event: right_click(0))
    # pola_gry[1].bind('<Button-3>', lambda event: right_click(1))
    # pola_gry[2].bind('<Button-3>', lambda event: right_click(2))
    # pola_gry[3].bind('<Button-3>', lambda event: right_click(3))
    # pola_gry[4].bind('<Button-3>', lambda event: right_click(4))
    # pola_gry[5].bind('<Button-3>', lambda event: right_click(5))
    # pola_gry[6].bind('<Button-3>', lambda event: right_click(6))
    # pola_gry[7].bind('<Button-3>', lambda event: right_click(7))
    # pola_gry[8].bind('<Button-3>', lambda event: right_click(8))
    # pola_gry[9].bind('<Button-3>', lambda event: right_click(9))
    # pola_gry[10].bind('<Button-3>', lambda event: right_click(10))
    # pola_gry[11].bind('<Button-3>', lambda event: right_click(11))
    # pola_gry[12].bind('<Button-3>', lambda event: right_click(12))
    # pola_gry[13].bind('<Button-3>', lambda event: right_click(13))
    # pola_gry[14].bind('<Button-3>', lambda event: right_click(14))
    # pola_gry[15].bind('<Button-3>', lambda event: right_click(15))
    # pola_gry[16].bind('<Button-3>', lambda event: right_click(16))
    # pola_gry[17].bind('<Button-3>', lambda event: right_click(17))
    # pola_gry[18].bind('<Button-3>', lambda event: right_click(18))
    # pola_gry[19].bind('<Button-3>', lambda event: right_click(19))
    # pola_gry[20].bind('<Button-3>', lambda event: right_click(20))
    # pola_gry[21].bind('<Button-3>', lambda event: right_click(21))
    # pola_gry[22].bind('<Button-3>', lambda event: right_click(22))
    # pola_gry[23].bind('<Button-3>', lambda event: right_click(23))
    # pola_gry[24].bind('<Button-3>', lambda event: right_click(24))
    # pola_gry[25].bind('<Button-3>', lambda event: right_click(25))
    # pola_gry[26].bind('<Button-3>', lambda event: right_click(26))
    # pola_gry[27].bind('<Button-3>', lambda event: right_click(27))
    # pola_gry[28].bind('<Button-3>', lambda event: right_click(28))
    # pola_gry[29].bind('<Button-3>', lambda event: right_click(29))
    # pola_gry[30].bind('<Button-3>', lambda event: right_click(30))
    # pola_gry[31].bind('<Button-3>', lambda event: right_click(31))
    # pola_gry[32].bind('<Button-3>', lambda event: right_click(32))
    # pola_gry[33].bind('<Button-3>', lambda event: right_click(33))
    # pola_gry[34].bind('<Button-3>', lambda event: right_click(34))
    # pola_gry[35].bind('<Button-3>', lambda event: right_click(35))
    # pola_gry[36].bind('<Button-3>', lambda event: right_click(36))
    # pola_gry[37].bind('<Button-3>', lambda event: right_click(37))
    # pola_gry[38].bind('<Button-3>', lambda event: right_click(38))
    # pola_gry[39].bind('<Button-3>', lambda event: right_click(39))
    # pola_gry[40].bind('<Button-3>', lambda event: right_click(40))
    # pola_gry[41].bind('<Button-3>', lambda event: right_click(41))
    # pola_gry[42].bind('<Button-3>', lambda event: right_click(42))
    # pola_gry[43].bind('<Button-3>', lambda event: right_click(43))
    # pola_gry[44].bind('<Button-3>', lambda event: right_click(44))
    # pola_gry[45].bind('<Button-3>', lambda event: right_click(45))
    # pola_gry[46].bind('<Button-3>', lambda event: right_click(46))
    # pola_gry[47].bind('<Button-3>', lambda event: right_click(47))
    # pola_gry[48].bind('<Button-3>', lambda event: right_click(48))
    # pola_gry[49].bind('<Button-3>', lambda event: right_click(49))
    # pola_gry[50].bind('<Button-3>', lambda event: right_click(50))
    # pola_gry[51].bind('<Button-3>', lambda event: right_click(51))
    # pola_gry[52].bind('<Button-3>', lambda event: right_click(52))
    # pola_gry[53].bind('<Button-3>', lambda event: right_click(53))
    # pola_gry[54].bind('<Button-3>', lambda event: right_click(54))
    # pola_gry[55].bind('<Button-3>', lambda event: right_click(55))
    # pola_gry[56].bind('<Button-3>', lambda event: right_click(56))
    # pola_gry[57].bind('<Button-3>', lambda event: right_click(57))
    # pola_gry[58].bind('<Button-3>', lambda event: right_click(58))
    # pola_gry[59].bind('<Button-3>', lambda event: right_click(59))
    # pola_gry[60].bind('<Button-3>', lambda event: right_click(60))
    # pola_gry[61].bind('<Button-3>', lambda event: right_click(61))
    # pola_gry[62].bind('<Button-3>', lambda event: right_click(62))
    # pola_gry[63].bind('<Button-3>', lambda event: right_click(63))


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

# def gorny_start():
#     aktualizacjaZegara(zegar)
#     aktualizacjaLicznikaMin(licznik_min)
#     panel_gorny=[zegar, licznik_min]
#     return panel_gorny
#
# def aktualizacjaZegara(zegar):
#     CZAS+=1
#     zegar["text"]="0"*(3-len(str(CZAS)))+str(CZAS)
#     root.after(1000, aktualizacjaZegara, zegar)
#
# def aktualizacjaLicznikaMin(licznik_min):
#     global LICZBAMIN
#     for mina in range (LICZBAMIN, -1):
#         print(mina)
# # dałabym tutaj odniesienie do funkcji oflagowania, gdzie jest wstępna liczba flag-- poziom łatwy, średni, trudny
#     licznik_min["text"]=LICZBAMIN

CZAS=0
LICZBAMIN=10
LICZBASZCZUROW=LICZBAMIN

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

# Inicjalizacja grafik panelu górnego
szczur = Image.open("Grafiki/szczur.png")
szczur = szczur.resize((40,40))
szczur = ImageTk.PhotoImage(szczur)

buzka1 = Image.open("Grafiki/buzka_usmiech.png")
buzka1 = buzka1.resize((40,40))
buzka1 = ImageTk.PhotoImage(buzka1)

buzka2 = Image.open("Grafiki/buzka_wow.png")
buzka2 = buzka2.resize((40,40))
buzka2 = ImageTk.PhotoImage(buzka2)

buzka3 = Image.open("Grafiki/buzka_smierc.png")
buzka3 = buzka3.resize((40,40))
buzka3 = ImageTk.PhotoImage(buzka3)

info_font = font.Font(family='Tahoma', size=20)
button_font = font.Font(family='Tahoma', size=20)

##### Uruchomienie wykonywania programu #####
welcome_panel()

root.mainloop()
