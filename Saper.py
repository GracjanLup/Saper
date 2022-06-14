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
    welcome = Label(main_panel, text="Witamy w grze Saper!", font=info_font, fg="#7F1734", bg="black")
    welcome.place(x=70, y=80)

    # difiniowanie przycisku do uruchomienia gry
    start_button = Button(main_panel, text='Start!', font=button_font, fg="#7F1734", bg="black", command=lambda:[start_button.place_forget(), welcome.place_forget(), set_level_of_game()])
    start_button.place(x=140, y=130)

##### Wybór poziomu trudności gry #####
def set_level_of_game():
    # definiowanie tekstu informacyjnego
    info_level = Label(main_panel, text="Wybierz poziom trudności gry:", font=info_font, fg="#7F1734", bg="black")
    info_level.place(x=30, y=80)

    global Try_number
    Try_number = 1

    ### Przyciski określające możliwe do wyboru poziomy gry ###
    # kliknięcie przycisku skutkuje uruchomieniem funkcji run_game z odpowiednimi parametrami
    # poziom łatwy
    level1 = Button(main_panel, text='ŁATWY', font=button_font, fg="#7F1734", bg="black", command=lambda:[level1.place_forget(), level2.place_forget(), info_level.place_forget(), run_game(10, 8, 8, "easy")])
    level1.place(x=130, y=120)

    # poziom trudny
    level2 = Button(main_panel, text='TRUDNY', font=button_font, fg="#7F1734", bg="black", command=lambda:[level1.place_forget(), level2.place_forget(), info_level.place_forget(), run_game(40, 16, 16, "hard")])
    level2.place(x=125, y=170)

##### Uruchomienie gry #####
def run_game(number_of_mines, number_of_rows, number_of_columns, level_game):

    # Zmiana planszy na trudną:
    if level_game == "hard":
        root.geometry('850x900')
        plotno.place_forget()
        plotno2.place(x=0, y=0)
        plotno2.create_image(420,460,image=obrazTk1)

        upper_panel.place(width=740, height=40, y=60, x=50)
        main_panel.place(width=737, height=737, y=130, x=50)
        emotikona.place(x=390, y=55)
        licznik_min.place(relx=0.25, y=0)

    # definiowanie zmiennej globalnej przechowującej informacje o poziomie trudności gry
    global level
    level = level_game

    # definiowanie łącznej ilości pól
    global number_of_fields
    number_of_fields = number_of_rows * number_of_columns

    # definicja zmiennej globalnej przechowującej pozycje min
    global mines_positions
    # wywołanie funkcji losującej pozycje min, przypisanie do zmiennej globalnej
    mines_positions = draw_of_mines(number_of_mines, number_of_fields)

    # odpalenie funkcji panelu górnego
    global Mine_number
    Mine_number = number_of_mines
    gorny_start()

    # definicja zmiennej globalnej przechowującej pola gry
    global pola_gry
    # przyciski posiadają unikalne identyfikatory
    # partial pozwala na uruchomienie funkcji z parametrem - w tym przypadku sprawdzającej właściwości pola
    # generowanie przycisków dla poziomu łatwego
    if level == "easy":
        pola_gry = [tk.Button(main_panel, image=test, bg="#141414", command=partial(check_position_easy, i)) for i in range(number_of_fields)]
    # generowanie przycisków dla poziomu trudnego
    else:
        pola_gry = [tk.Button(main_panel, image=test, bg="#141414", command=partial(check_position_hard, i)) for i in range(number_of_fields)]

    # rysowanie planszy
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            pola_gry[i * number_of_columns + j].grid(row = j, column = i)
            pola_gry[i * number_of_columns + j].bind('<Button-3>', right_click)

##### Sprawdzanie pól dla poziomu łatwego - czy mina, sprawdzanie sąsiadów #####
def check_position_easy(i):
    # Tylko przy pierwszym kliknięciu odsłoń zera i daj punkty
    global Punkty
    if Punkty == 0:
        ZeroCheck("easy")
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
        lose_game(i)
    else:
        Punkty+=1
        emotikona.config(image=buzka2)
        emotikona.after(300, aktualizujEmotke)
        pola_gry[i].unbind('<Button-3>')
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
        # sprawdzenie czy to wszystkie pola
        if Punkty == 54:
            win_game()
        # funkcja przypisująca odpowiedni obrazek prezentujący cyfrę
        # zależność od ilości posiadanych bomb jako sąsiadów
        set_image_of_number(i, count)

##### Sprawdzanie pól dla poziomu trudnego - czy mina, sprawdzanie sąsiadów #####
def check_position_hard(i):
    # Tylko przy pierwszym kliknięciu odsłoń zera i daj punkty
    global Punkty
    if Punkty == 0:
        ZeroCheck("hard")
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
        lose_game(i)
    else:
        Punkty+=1
        emotikona.config(image=buzka2)
        emotikona.after(300, aktualizujEmotke)
        pola_gry[i].unbind('<Button-3>')
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
        if Punkty == 216:
            win_game()
        # funkcja przypisująca odpowiedni obrazek prezentujący cyfrę
        # zależność od ilości posiadanych bomb jako sąsiadów
        set_image_of_number(i, count)

##### Przypisywanie obrazka prezentującego cyfrę - zależność od posiadanych bomb sąsiadów #####
def set_image_of_number(i, count):
    # liczba bomb 1 - przypisz obrazek cyfra1
    if count == 1:
        pola_gry[i].config(image=cyfra1, command='')
    # analogicznie jak wyżej
    elif count == 2:
        pola_gry[i].config(image=cyfra2, command='')
    elif count == 3:
        pola_gry[i].config(image=cyfra3, command='')
    elif count == 4:
        pola_gry[i].config(image=cyfra4, command='')
    elif count == 5:
        pola_gry[i].config(image=cyfra5, command='')
    elif count == 6:
        pola_gry[i].config(image=cyfra6, command='')
    elif count == 7:
        pola_gry[i].config(image=cyfra7, command='')
    elif count == 8:
        pola_gry[i].config(image=cyfra8, command='')
    elif count == 0:
        pola_gry[i].config(image=cyfra0, command='')

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
def lose_game(i):
    global Defeat
    Defeat = 1
    emotikona.config(image=buzka4)
    mines_positions.remove(i)
    for i in range(len(pola_gry)):
        pola_gry[i].config(command='')
        pola_gry[i].unbind('<Button-3>')
    for j in mines_positions:
        pola_gry[j].config(image=mina)

def win_game():
    global Timer
    messagebox.showinfo("Win", f"Wygrałeś! Twój czas to {Timer}s")

##### Prawe kliknięcie myszy #####
def right_click(event):
    aktualizacjaLicznikaMin(licznik_min, 1)
    # usunięcie możliwości sprawdzenia pozycji przy ustawionej fladze
    event.widget.configure(image = rat, command = '')
    # zbindowanie na prawym przycisku funkcji reset
    event.widget.bind('<Button-3>', reset)

##### Ponowne kliknięcie prawego przycisku myszy - usunięcie flagi #####
def reset(event):
    aktualizacjaLicznikaMin(licznik_min, 2)
    # sprawdzene indeksu dla klikniętego widgetu w liście
    index_of_button = pola_gry.index(event.widget)
    # w zależności od levelu przypisujemy na nowo obrazek i wywoływaną funkcję po kliknięciu
    if level == "easy":
        event.widget.configure(image = test, command = partial(check_position_easy, index_of_button))
    else:
        event.widget.configure(image=test, command=partial(check_position_hard, index_of_button))
    # zbindowanie na prawym przycisku funkcji right_click
    event.widget.bind('<Button-3>', right_click)

# Start panelu głównego - Emma:
def gorny_start():
    global Try_number
    if Try_number == 1:
        aktualizacjaZegara(zegar)
    Try_number += 1
    aktualizacjaLicznikaMin(licznik_min, 0)
    panel_gorny=[zegar, licznik_min]
    return panel_gorny

# Zegar - Emma:
def aktualizacjaZegara(zegar):
    global Timer
    Timer+=1
    zegar["text"]="0"*(3-len(str(Timer)))+str(Timer)
    root.after(1000, aktualizacjaZegara, zegar)

# Licznik min - Emma:
def aktualizacjaLicznikaMin(licznik_min, variable):
    global Mine_number
    # for mina in range (LICZBAMIN, -1):
    #     print(mina)
    if variable == 0:
        licznik_min["text"]=Mine_number
    elif variable == 1:
        Mine_number -= 1
        licznik_min["text"]=Mine_number
    elif variable == 2:
        Mine_number += 1
        licznik_min["text"]=Mine_number

# Powrót do uśmiechniętej - Emma
def aktualizujEmotke():
    emotikona.config(image=buzka1)

# Kliknięcie buźki - Emma (i restart gry)
def ClickEmotke():
    global Punkty, Defeat, Timer
    if level == "easy":
        if Punkty >= 54 or Defeat == 1:
            Punkty = 0
            Timer = 0
            # for i in range(len(pola_gry)):
            #     pola_gry[i].config(main_panel, image=test, bg="#141414", command=partial(check_position_easy, i))
            run_game(10, 8, 8, "easy")
        else:
            emotikona.config(image=buzka3)
            emotikona.after(150, aktualizujEmotke)
    else:
        if Punkty >= 216 or Defeat == 1:
            Punkty = 0
            Timer = 0
            run_game(40, 16, 16, "hard")
            # for i in range(len(pola_gry)):
            #     pola_gry[i].config(main_panel, image=test, bg="#141414", command=partial(check_position_easy, i))
        else:
            emotikona.config(image=buzka3)
            emotikona.after(150, aktualizujEmotke)


def ZeroCheck(level):
    for i in range (number_of_fields):
        if level == "easy":
            numbers = [i - 9, i - 8, i - 7, i - 1, i + 1, i + 7, i + 8, i + 9]
        else:
            numbers = [i - 17, i - 16, i - 15, i - 1, i + 1, i + 15, i + 16, i + 17]
        count = 0
        for x in numbers:
            if x in mines_positions:
                count += 1
        if count == 0:
            if i in mines_positions:
                None
            else:
                pola_gry[i].config(image=cyfra0, command='')
                global Punkty
                Punkty += 1

Timer = 0
Punkty = 0

root = tk.Tk()
root.title('Minesweeper')
root.geometry('400x450')

info_font = font.Font(family='Tahoma', size=16)
button_font = font.Font(family='Tahoma', size=16)

# płótno ramki tylniej
plotno=Canvas(root, width=400, height=450)
plotno.place(x=0, y=0)

plotno2=Canvas(root, width=850, height=900)

# definiowanie wyglądu - panel górny
upper_panel = tk.Frame(root, bg="black")
upper_panel.place(width=360, height=34, y=22, x=20)

# Zegar:
zegar = tk.Label(upper_panel, bg="black", fg="red", font=("Digital-7", 20), borderwidth=2, relief="raised")
zegar.place(relx=0.67, y=0)
zegar["text"]="001"

# Licznik min:
licznik_min = tk.Label(upper_panel, bg="black", fg="red", font=("Digital-7", 20), borderwidth=2, relief="raised")
licznik_min.place(relx=0.2, y=0)
licznik_min["text"]="001"

# Buźka:
buzka1 = Image.open("Grafiki/buzka_usmiech.png")
buzka1 = buzka1.resize((40,40))
buzka1 = ImageTk.PhotoImage(buzka1)
emotikona=tk.Button(root, width=40, height=40, image=buzka1, bg="#141414", command=ClickEmotke)
emotikona.place(x=180, y=20)

buzka2 = Image.open("Grafiki/buzka_wow.png")
buzka2 = buzka2.resize((40,40))
buzka2 = ImageTk.PhotoImage(buzka2)

buzka3 = Image.open("Grafiki/buzka_zla.png")
buzka3 = buzka3.resize((40,40))
buzka3 = ImageTk.PhotoImage(buzka3)

buzka4 = Image.open("Grafiki/buzka_smierc.png")
buzka4 = buzka4.resize((40,40))
buzka4 = ImageTk.PhotoImage(buzka4)

# definiowanie wyglądu - panel dolny
main_panel = tk.Frame(root, bg="black")
main_panel.place(width=360, height=365, y=65, x=20)

obraz = Image.open("Grafiki/test.png")
obraz = obraz.resize((40,40))
test = ImageTk.PhotoImage(obraz)

# definiowanie płótna - ramki
obraz=Image.open("Grafiki/ramka.png")
# obraz = obraz.resize((400, 450))
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,230,image=obrazTk)

# definiowanie płótna - ramki na poziom trudny
obraz1=Image.open("Grafiki/ramka1.png")
obraz1 = obraz1.resize((850, 900))
obrazTk1=ImageTk.PhotoImage(obraz1)

# inicjalizacja grafiki dla bomby
mina = Image.open("Grafiki/bomba.png")
mina = mina.resize((40,40))
mina = ImageTk.PhotoImage(mina)

mina_red = Image.open("Grafiki/bomba_red.png")
mina_red = mina_red.resize((40,40))
mina_red = ImageTk.PhotoImage(mina_red)

# inicjalizacja grafiki dla szczura
rat = Image.open("Grafiki/rat.png")
rat = rat.resize((40,40))
rat = ImageTk.PhotoImage(rat)

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

cyfra6 = Image.open("Grafiki/6.png")
cyfra6 = cyfra6.resize((40,40))
cyfra6 = ImageTk.PhotoImage(cyfra6)

cyfra7 = Image.open("Grafiki/7.png")
cyfra7 = cyfra7.resize((40,40))
cyfra7 = ImageTk.PhotoImage(cyfra7)

cyfra8 = Image.open("Grafiki/8.png")
cyfra8 = cyfra8.resize((40,40))
cyfra8 = ImageTk.PhotoImage(cyfra8)

cyfra0 = Image.open("Grafiki/0.png")
cyfra0 = cyfra0.resize((40,40))
cyfra0 = ImageTk.PhotoImage(cyfra0)


##### Uruchomienie wykonywania programu #####
welcome_panel()

root.mainloop()
