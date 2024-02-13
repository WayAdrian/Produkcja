
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

def next():
    f.jeden('enter')
    f.kilka(1, 'down')
    f.jeden('enter')
    f.kilka(1, 'down')


f.aktywacja()


# #
# #
# # dodaje dostawce
f.operacje('p', 'k')
f.jeden('insert')
f.time.sleep(3)
f.kilka(1, 'tab')
f.kilka(1, 'down') # typ dostawca
f.kilka(29, 'tab')
f.tekst('D-' + dzis)
f.kilka(2, 'tab')
f.dwa('shift', 'o')
f.kilka(1, 'right')
f.dwa('ctrl', 'c')
dostawca = pyperclip.paste()
time.sleep(3)

#odbiorce
f.jeden('insert')
time.sleep(1)
f.kilka(30, 'tab')
f.tekst('O-' + dzis)
f.kilka(1, 'tab')
for i in range(2):
    keyboard.press_and_release('ctrl+tab')
f.time.sleep(0.5)
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(0.5)
f.kilka(1,'tab')
f.tekst('Warszawa')
for i in range(1):
    keyboard.press_and_release('ctrl+tab')
f.dwa('shift', 'o')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
time.sleep(1)
f.dwa('ctrl', 'c')
odbiorca = pyperclip.paste()
f.jeden('esc')
print(dostawca, odbiorca)
#############################################################

# Dodanie artykułu: Towar T1 SZT
f.operacje('p', 'a')
f.jeden('insert')
f.time.sleep(3)
f.tekst('T1')
f.kilka(1, 'tab')
f.tekst('T1')
f.kilka(11, 'tab')
f.tekst('SZT')
f.kilka(1, 'tab')
f.dwa('shift', 'o')

# Dodanie artykułu Surowiec S1 KG + Dostawca
f.jeden('insert')
f.time.sleep(1)
f.tekst('S1')
f.kilka(1, 'tab')
f.tekst('S1')
f.kilka(2, 'tab')
f.kilka(2, 'down')
f.kilka(9, 'tab')
f.tekst('KG')
f.kilka(1, 'tab')
for i in range(6):
    keyboard.press_and_release('ctrl+tab')
    f.time.sleep(0.1)
f.kilka(1, 'tab')
f.jeden('insert')
f.tekst(dostawca) # tu bedzie później dostawca
f.kilka(2, 'tab')
f.tekst('55')
f.kilka(3, 'tab')
f.tekst('1234')
f.kilka(1, 'tab')
f.tekst('1234')
f.kilka(4, 'tab')
f.jeden('spacja')
f.dwa('shift', 'o')
f.kilka(3, 'tab')
f.dwa('shift', 'o')


# Dodaje wyrób
# Uzupełniam dane podstawowe
f.jeden('insert')
f.time.sleep(1)
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('W1')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(9, 'tab')
f.tekst('SZT')
f.kilka(1, 'tab')
#Przeskakuje na karte Inne
f.zakladka(8)
# Zaznaczam checkbox "numery seryjne"
f.kilka(1, 'tab')
f.jeden('spacja')
f.kilka(1, 'tab')
f.jeden('spacja')
f.kilka(7, 'tab')
f.tekst('13')
f.kilka(1, 'tab') # zatwierdzam ale to do usuniecia jak w 007 bedzie poprawione partie
f.dwa('shift', 'o')
f.time.sleep(1)


# checkbox obsługa partii
# for i in range(3):
#     keyboard.press_and_release('ctrl+tab')
#     f.time.sleep(0.1)
# f.kilka(7, 'tab'
# f.jeden('spacja')



#### DOdaje technologie i operacje !!!!!!!!!!
# Dodaje Półprodukt
f.jeden('insert')
f.time.sleep(1)
f.tekst('PP1')
f.kilka(1, 'tab')
f.tekst('PP1')
f.kilka(2, 'tab')
f.kilka(5, 'down')
f.kilka(9, 'tab')
f.tekst('SZT')
f.kilka(1, 'tab')
f.dwa('shift', 'o')


f.time.sleep(1)
f.jeden('f12')
f.kilka(34, 'down')
f.jeden('enter')
# dane podstawowe technologii
f.dwa('ctrl', 'a')
f.tekst('PP1')
f.time.sleep(2)
f.kilka(1, 'tab')
f.tekst('PP1')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(1, 'tab')

f.zakladka(1)
#zakładka operacje
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.jeden('insert')
f.time.sleep(1)
# nowa operacja
f.kilka(2, 'tab')
f.tekst('OP')
f.kilka(2, 'tab')
f.time.sleep(1)
f.zakladka(4)
#zakładka wyroby gotowe
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.tekst('PP1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
#zatwierdzenie operacji
f.dwa('shift', 'o')
f.time.sleep(1)
# wchodze jeszcze raz w operacje
f.jeden('f5')
f.time.sleep(1.5)
f.kilka(4, 'tab')
f.zakladka(3)
#zakładka surowce dodaje
f.kilka(1, 'tab')
f.jeden('insert')
f.tekst('S1')
f.kilka(1, 'tab')
f.tekst('3')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.kilka(11, 'tab')
f.kilka(1, 'down')
f.time.sleep(1)
f.dwa('shift', 't')
f.kilka(3, 'tab')
f.dwa('shift', 'o')

################################################  tchno dla wyrobu W
f.kilka(1, 'up')
f.jeden('f12')
f.time.sleep(0.5)
f.kilka(34, 'down')
f.jeden('enter')
f.dwa('ctrl', 'a')
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('W1')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(3, 'tab')
f.tekst('40')
# ZAKŁAdka Operacje!!!!!!!!
f.zakladka(1)
#zakładka operacje
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.jeden('insert')
f.time.sleep(1)
# nowa operacja
f.kilka(2, 'tab')
f.tekst('OP2')
f.kilka(2, 'tab')
f.zakladka(4)
#zakładka wyroby gotowe
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
#zatwierdzenie operacji
f.dwa('shift', 'o')
f.time.sleep(1)
# wchodze jeszcze raz w operacje
f.jeden('f5')
f.time.sleep(1.5)
f.kilka(2, 'tab')
f.zakladka(3)
#zakładka surowce dodaje
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(0.5)
f.tekst('S1')
f.kilka(1, 'tab')
f.tekst('2')
f.kilka(1, 'tab')
f.dwa('shift', 'o')

f.time.sleep(1)
f.jeden('insert')
f.time.sleep(0.5)
f.tekst('PP1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(1, 'tab')
f.dwa('shift', 'o')

f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.kilka(11, 'tab')
f.kilka(1, 'down')
f.time.sleep(1)
f.dwa('shift', 't')
f.kilka(3, 'tab')
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('esc')

f.updatesql()

######################## technologia dla półproduktu















# automatycznie generuj dok. rozchodowe   auto_dok_r
# automatycznie pobierz załącnziki
# autmatycznie uaktualnij stany mag. wyrobu auto_prz_p
# automatycznie uaktualnij stany mag. braków auto_prz_b
# automatycznie uaktualnij stany mag. odpadów auto_prz_o



