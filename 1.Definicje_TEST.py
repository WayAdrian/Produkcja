import Functions as f
import datetime
import time
import pyautogui
import keyboard
import time
import pyperclip
import pytest
import sys
import datetime
import pyodbc



today = str(datetime.date.today())
dzis = today.replace("-", "")
f.pyautogui.PAUSE = 1
poczatek_testu = time.time()

f.nowytxt() # dodaje plik txt dla raportu
f.doplikutxt("\n Kartoteka ")


f.aktywacja()




def next():
    '''
    :return:  powtarzalny kod do wskazania rejestrów definicji ZPR
    '''
    f.jeden('enter')
    f.kilka(1, 'down')
    f.jeden('enter')
    f.kilka(1, 'down')



# Definicja ZZ ustawienie dok. do przkesztacenia =PZ
f.operacje('o', 'd')
f.kilka(12, 'down')
f.kilka(2, 'right')
def sprWZ():

    f.dwa('ctrl', 'c')
    rej = f.pyperclip.paste()
    if rej == 'Wydania na zewnątrz                               ':
        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(3, 'tab')
        f.kilka(17, 'down')
        f.dwa('ctrl', 'c')
        wla = f.pyperclip.paste()

        while wla != 'Przekształcany w dokument                                                                           ':

            f.kilka(1, 'down')
            f.dwa('ctrl', 'c')
            wla = f.pyperclip.paste()

        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(1, 'tab')
        f.kilka(1,'down')# ustawiam do przkesztacenia PZ
        f.kilka(1, 'tab')
        f.jeden('enter')
        f.kilka(1, 'tab')
        f.dwa('shift', 'o')
    else:
        f.kilka(1, 'down')
        sprWZ()


def sprZS():

    f.dwa('ctrl', 'c')
    rej = f.pyperclip.paste()
    if rej == 'Zamówienie na sprzedaż                            ':
        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(3, 'tab')
        f.kilka(16, 'down')
        f.dwa('ctrl', 'c')
        wla = f.pyperclip.paste()


        while wla != 'Przekształcany w dokument                                                                           ':

            f.kilka(1, 'down')
            f.dwa('ctrl', 'c')
            wla = f.pyperclip.paste()

        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(1, 'tab')
        f.kilka(1,'down')# ustawiam do przkesztacenia PZ
        f.kilka(1, 'tab')
        f.jeden('enter')
        f.kilka(1, 'tab')
        f.dwa('shift', 'o')

    else:
        f.kilka(1, 'down')
        sprZS()


def sprWD():
    f.dwa('ctrl', 'c')
    rej = f.pyperclip.paste()
    if rej == 'Zlecenia wydania                                  ':
        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(3, 'tab')
        f.kilka(20, 'down')
        f.dwa('ctrl', 'c')
        wla = f.pyperclip.paste()

        while wla != 'Generuj dokumenty                                                                                   ':

            f.kilka(1, 'down')
            f.dwa('ctrl', 'c')
            wla = f.pyperclip.paste()

        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(1, 'tab')
        f.kilka(1, 'down')  # ustawiam do przkesztacenia PZ
        f.kilka(1, 'tab')
        f.jeden('enter')

        f.kilka(1, 'tab')
        f.dwa('shift', 'o')

    else:
        f.kilka(1, 'down')
        sprWD()


def dodR():
    '''
    :return: Funkcja dodaje rejestr R/P i ustawia na nim: rodzaj ceny- zakup netto, dokumen produkcyjny - tak.
    '''
    f.jeden('insert')
    f.time.sleep(1)
    f.tekst('R')
    f.kilka(1, 'tab')
    f.tekst('P')
    f.kilka(1, 'tab')
    f.tekst('Rozchód produkcyjny')
    f.kilka(3, 'tab')
    f.dwa('ctrl', 'c')
    dokpro = f.pyperclip.paste()
    while dokpro != 'Dokument produkcyjny                                                                                ':
        f.kilka(1, 'down')
        f.dwa('ctrl', 'c')
        dokpro = f.pyperclip.paste()

    f.jeden('enter')
    f.time.sleep(1)
    f.kilka(1, 'up')
    f.kilka(1, 'tab')
    f.dwa('shift', 'o')
    f.time.sleep(1)
    f.kilka(1, 'down')

    f.dwa('ctrl', 'c')
    rodzceny = f.pyperclip.paste()
    while rodzceny != 'Rodzaj ceny                                                                                         ':
        f.kilka(1, 'down')
        f.dwa('ctrl', 'c')
        rodzceny = f.pyperclip.paste()

    f.jeden('enter')
    f.time.sleep(1)
    f.kilka(2, 'down')
    f.kilka(2, 'tab')
    f.dwa('shfit', 'o')
    f.time.sleep(0.3)
    f.kilka(1, 'tab')
    f.dwa('shift', 'o')


def dodP():
    '''
    :return: Funkcja dodaje rejestr P/P i ustawia na nim: dokumen produkcyjny - tak.
    '''
    f.jeden('insert')
    f.time.sleep(1)
    f.tekst('P')
    f.kilka(1, 'tab')
    f.tekst('P')
    f.kilka(1, 'tab')
    f.tekst('Przychód produkcyjny')
    f.kilka(3, 'tab')
    f.dwa('ctrl', 'c')
    dokpro = f.pyperclip.paste()
    while dokpro != 'Dokument produkcyjny                                                                                ':
        f.kilka(1, 'down')
        f.dwa('ctrl', 'c')
        dokpro = f.pyperclip.paste()

    f.jeden('enter')
    f.time.sleep(1)
    f.kilka(1, 'up')
    f.kilka(1, 'tab')
    f.dwa('shift', 'o')
    f.time.sleep(1)
    f.kilka(1, 'tab')
    f.dwa('shift', 'o')


sprWZ()
f.kilka(20, 'down')
sprZS()
f.kilka(11, 'tab')
sprWD()
dodR()
dodP()

f.jeden('esc')


f.dwa('shift', 'alt')
f.kilka(21, 'down')
f.kilka(1, 'right')
f.kilka(20, 'down')
f.jeden('enter')
f.time.sleep(0.5)

f.jeden('insert')
f.time.sleep(0.5)
f.tekst('1')
f.kilka(1, 'tab')
f.tekst('ZPR')
f.kilka(1, 'tab')
f.kilka(2, 'down')
#Przychód wyrobów gotowych
for i in range (12):
    next()

f.kilka(9, 'down')
f.jeden('enter')
f.kilka(1, 'down')
f.jeden('enter')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.jeden('esc')















