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


# 1.A Wchodze w definicje dokmentów - funkcja sprWZ, szuka definicji dokmentu WZ i ustawia na nim
        # rejestr do przekształceń
# 1.B Wchodze w definicje dokmentów - funkcja sprZS, szuka definicji dokmentu ZS i ustawia na nim
        # rejestr do przekształceń
# 1.C Wchodzę w definicje dokumetów - funkcja sprWD, szuka definicji dokumentu WD i ustawia na nim rejestr
        # do wygenerowanego dokumentu
# 1.D Dodaje definicje dokmentu R - ustawiam na nim, że to dokumet produkcyjny
# 1.E Dodaje definicje dokumentu P - ustawiam na nim, że to dokument produkcyjny
# 1.F Dodaje rejstr ZPR i ustawiam na nim magazyny dla przychodó i rozchodów oraz ustawiam zapotrzebowanie
        # przy generowaniu na NIE

today = str(datetime.date.today())
dzis = today.replace("-", "")
f.pyautogui.PAUSE = 1
poczatek_testu = time.time()

f.nowytxt() # dodaje plik txt dla raportu



f.aktywacja()


def next():
    '''
    :return:  powtarzalny kod do wskazania rejestrów definicji ZPR
    '''
    f.jeden('enter')
    f.kilka(1, 'down')
    f.jeden('enter')
    f.kilka(1, 'down')




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
        f.kilka(12, 'down')
        f.kilka(1, 'tab')
        f.kilka(1,'down')
        f.kilka(1, 'tab')
        f.kilka(1, 'tab')
        f.dwa('shift', 'o')
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

#1.A

f.operacje('o', 'd')
f.kilka(10, 'down')
f.kilka(2, 'right')

sprWZ()
f.kilka(20, 'down')

#1.B
sprZS()

#1.C
sprWD()

#1.D
dodR()

#1.E
dodP()

f.jeden('esc')

#1.F
f.dwa('shift', 'alt')
#f.kilka(21, 'down')
f.kilka(20, 'down') # maszynka
f.kilka(1, 'right')
#f.kilka(20, 'down')
f.kilka(18, 'down') # maszynka
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















