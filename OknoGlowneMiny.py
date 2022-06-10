import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter
from functools import partial

class AplikacjaGUI(Frame, object):
    def __init__ (self, master):
        super(AplikacjaGUI, self).__init__(master)
        self.master.title("Saper")
        self.master.geometry("1200x800")
        self.grid()
        # Przekierowanie do panelu powitalnego:
        self.welcome_panel()

    def hide_all_widgets(self):
        for widgets in self.winfo_children():
            widgets.destroy()

    def set_level_of_game(self):
        info_font = font.Font(family='Tahoma', size=20)
        info = Label(text="Wybierz poziom trudności gry:", font=info_font)
        info.pack()

    def welcome_panel(self):
        info_font = font.Font(family='Tahoma', size=20)
        button_font = font.Font(family='Tahoma', size=20)

        welcome=Label(self, text="Witamy w grze Saper!", font=info_font)
        welcome.pack()

        startButton = Button(self, text='Start!', font=button_font, command=lambda:[self.hide_all_widgets(), self.set_level_of_game()])
        startButton.pack()


def main():
    root=tk.Tk()

    info_font = font.Font(family='Tahoma', size=20)
    button_font = font.Font(family='Tahoma', size=20)

    app=AplikacjaGUI(root)
    root.mainloop()

main()
