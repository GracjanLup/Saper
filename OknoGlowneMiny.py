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
    # for j in range(number_of_columns*number_of_rows):
    #     pola_gry[j].bind('<Button-3>', lambda event: right_click(j))
    #     pola_gry[j].focus_set()
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

# sprawdzenie pozycji po kliknięciu - czy bomba czy wyświetlić liczbę
# do dokończenia sprawdzanie sąsiadów w przypadku, gdy kliknięty przycisk jest przy krawędzi
# oraz pojawianie się pól, gdy wartość jest równa 0
def check_position(i):
    count = 0
    print(i)
    if i in mines_positions:
        pola_gry[i].config(image=mina_red)
        end_game(i)
    else:
        numbers = [i - 9, i - 8, i - 7, i - 1, i + 1, i + 7, i + 8, i + 9]
        for x in numbers:
            if x in mines_positions:
                count += 1
        # warunek tego ile jest bomb do okoła - wstawia odpowiednie zdjęcie
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

# funkcja końca gry
def end_game(i):
    print("Przegrałeś")
    mines_positions.remove(i)
    for i in range(len(pola_gry)):
        pola_gry[i].config(command='')
    for j in mines_positions:
        pola_gry[j].config(image=mina)

# funkcja prawego przycisku myszy
def right_click(a):
    # print(a)
    pola_gry[a].config(image=flaga, command='')
    pola_gry[a].bind('<Button-3>', lambda event: reset(a))

# Ponowne wciesnięcie prawego przycisku myszy
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

# uruchomienie wykonywania programu
welcome_panel()

root.mainloop()
