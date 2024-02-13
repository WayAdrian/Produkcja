import Functions as f

# Spis

# 4.A - Wejście w moduł zamówienia, wejscie w wygenerowane zamówienie ZZ, ustawinie ceny zakupu,
        # w pozostałych danych ustawienie rejestu PZ/1 do przekształcenia, ustawineie statusu, zatwierdzenie i przekształcenie dokumentu.

# 4.B - Wejscie w przekształcony dokument PZ, dodanie artykulu T1, zatwierdzenie.




## 4.A
f.aktywacja()
f.time.sleep(1)
f.dwa('shift', 'alt')
f.kilka(17, 'down')
f.kilka(1, 'right')
f.kilka(5, 'down')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.kilka(5, 'tab')
f.tekst('1')
f.kilka(4, 'tab')
f.dwa('shift', 'o')

f.kilka(8, 'tab')
f.jeden('enter')
f.time.sleep(0.5)
f.kilka(1, 'tab')
f.kilka(1, 'down')
f.kilka(6, 'tab')
f.jeden('enter')
f.kilka(5, 'tab')
f.kilka(1, 'down')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.jeden('spacja')
f.przeksztalc()
f.time.sleep(0.5)
f.dwa('shift', 'T')
f.time.sleep(0.5)
f.dwa('shift', 'T')
f.time.sleep(2)
for i in range(3):
    f.jeden('esc')
    f.time.sleep(0.3)


## 4.B
f.operacje('z', 'p')
f.time.sleep(0.5)
f.jeden('enter')
f.time.sleep(0.5)

f.jeden('insert')
f.time.sleep(1)
f.kilka(1, 'tab')
f.tekst('T1')
f.kilka(1, 'tab')
f.tekst('2000')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(4, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
f.dwa('shift', 'o')
f.jeden('esc')