import Functions as f

# 5.A - Wejście w Plany Produkcyjne, edycja planu, wejscie w podsumowanie, ustawienie rejestru, zaznaczenie artykułów,
        # wskazanie odbiorycy, generowanie ZPR

# 5.B - Rozlicz - wejscie w pierwszy dokument ZPR (PP1)- ustawiam status: Przekazane do produkcji, zaznaczam art i spod f12
        # melduje

# 5.B - Rozlicz - wejscie w drugi dokument ZPR (W1) - ustawiam status: Przekazane do produkcji, zaznaczam art i spod f12
        # melduje


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
f.kilka(8, 'tab')
f.jeden('enter')
f.time.sleep(0.5)
f.kilka(1, 'down')
f.kilka(3, 'tab')
f.tekst('00003')
f.kilka(3, 'tab')
f.jeden('spacja')
f.kilka(1, 'down')
f.jeden('spacja')
f.kilka(3, 'tab')
f.kilka(1, 'down')
f.kilka(1, 'tab')
f.jeden('enter')
f.time.sleep(2)
for i in range(4):
    f.jeden('esc')
    f.time.sleep(0.3)

f.aktywacja()
f.dwa('shift', 'alt')
#f.kilka(23, 'down')
f.kilka(22, 'down')
f.kilka(1, 'right')
f.jeden('enter')
f.time.sleep(1)
f.kilka(1, 'up')
f.jeden('enter')

f.time.sleep(3)
f.kilka(19, 'tab')
f.kilka(1, 'down')
f.kilka(9, 'tab')
f.jeden('f12')
f.kilka(7, 'down')
f.jeden('enter')
f.time.sleep(1)
f.tekst('123')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(6)
# wygenruja sie: R /P  /24/000001, R /P  /24/000001
for i in range(4):
    f.jeden('esc')
    f.time.sleep(0.3)


f.aktywacja()
f.dwa('shift', 'alt')
f.kilka(23, 'down')
f.kilka(1, 'right')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')

f.time.sleep(3)
f.kilka(19, 'tab')
f.kilka(1, 'down')
f.kilka(9, 'tab')
f.jeden('f12')
f.kilka(7, 'down')
f.jeden('enter')
f.time.sleep(1)
f.tekst('123')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(8)
# wygenruja sie: R /P  /24/000001, R /P  /24/000001
for i in range(4):
    f.jeden('esc')
    f.time.sleep(0.3)
# asercja sprawdzająca P i R
