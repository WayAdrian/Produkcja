
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

dzis = datetime.date.today()
jutro = dzis + datetime.timedelta(days=1)
dzis_formatowana = jutro.strftime("%d-%m-%Y")
print("Dzisiejsza data to:", dzis_formatowana)
f.aktywacja()


f.dwa('shift', 'alt')
f.kilka(3, 'down')
f.kilka(1, 'right')
f.kilka(5, 'down')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.kilka(10, 'tab')
f.kilka(1, 'down')
f.kilka(1, 'tab')
f.kilka(1, 'down')
f.kilka(3, 'tab')
f.zakladka(2)
f.kilka(2,'down')
f.time.sleep(1)
f.jeden('insert')
f.time.sleep(2)
f.tekst('T1')
f.kilka(1, 'tab')
f.time.sleep(0.5)
f.tekst('1')
f.kilka(1,'tab')
f.dwa('shift', 'n')
f.jeden('enter')
f.tekst('W1')
f.kilka(1, 'tab')
f.time.sleep(0.5)
f.tekst('10')
f.kilka(1,'tab')

f.dwa('shift', 'o')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(0.5)
f.kilka(1, 'tab')
f.jeden('enter')
f.kilka(1, 'tab')
f.jeden('enter')
f.kilka(2, 'tab')
f.tekst('10')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.kilka(1, 'tab')
f.jeden('enter')
f.dwa('shift', 'o')
f.kilka(11, 'tab')
f.kilka(2, 'down')
f.kilka(1, 'tab')
f.dwa('shift', 'g')
f.time.sleep(0.5)
f.dwa('shift', 't')
f.time.sleep(0.5)
f.dwa('shift', 'n')
f.time.sleep(0.5)
f.dwa('shift', 't')
f.time.sleep(0.5)
f.dwa('shift', 'p')
f.time.sleep(3)
for i in range(4):
    f.jeden('esc')
    f.time.sleep(0.3)

# asercja sprawdzająca wygenerowany dokument WZ

f.aktywacja()
f.operacje('s', 'w')
f.time.sleep(2)
f.jeden('spacja')
f.przeksztalc()
for i in range(3):
    f.jeden('esc')
    f.time.sleep(0.3)

# asercja sprawdzajaca dokument F