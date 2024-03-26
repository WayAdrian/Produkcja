
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





f.aktywacja()



# 3.A
f.dwa('shift', 'alt')
#f.kilka(17, 'down')
f.kilka(16, 'down')
f.kilka(1, 'right')
f.kilka(2, 'down')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.kilka(1, 'up')
f.jeden('spacja')
f.jeden('f12')
#f.kilka(22, 'down')
f.kilka(21, 'down')
f.jeden('enter')
f.time.sleep(1)
f.kilka(1, 'tab')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(0.5)
f.kilka(3, 'down')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(2, 'tab')
f.jeden('spacja')
f.kilka(1, 'tab')
f.jeden('enter')
f.time.sleep(3)
f.jeden('esc')
f.dwa('shift', 'o')
f.jeden('esc')
f.jeden('esc')


################ Plan Produkcji - Edycja - Generowanie ##
f.time.sleep(1)
f.aktywacja()
f.dwa('shift', 'alt')
#f.kilka(22, 'down')
f.kilka(21, 'down')
f.kilka(1, 'right')
f.kilka(10, 'down')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(2)
f.kilka(9, 'tab')
f.jeden('enter')
f.time.sleep(2)
f.dwa('shift', 'o')
f.kilka(18, 'tab')
f.jeden('spacja')
f.kilka(1, 'down')
f.jeden('spacja')
f.kilka(1, 'down')
f.jeden('spacja')
f.kilka(1, 'down')
f.jeden('spacja')
f.kilka(3, 'tab')
f.jeden('enter')
f.time.sleep(1)
f.jeden('esc')
f.kilka(16, 'tab')
f.zakladka(1)
f.kilka(2, 'tab')
f.jeden('enter')
f.kilka(1, 'tab')
f.jeden('spacja')
f.kilka(7, 'tab')
f.kilka(1, 'down')
f.kilka(6, 'tab')
f.tekst('M00001')
f.kilka(8, 'tab')
f.jeden('enter')

f.time.sleep(2)
for i in range(5):
    f.jeden('esc')
    time.sleep(0.2)

