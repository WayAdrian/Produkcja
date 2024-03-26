
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




D='D-' + dzis

def sprawdz_dokument(typ_ktr, nazwa_ktr):
    zapytanie = "SELECT typ_ktr, Nazwa_ktr FROM kontrah WHERE Nazwa_ktr = ? AND TYP_KTR = ?;"
    f.cursor.execute(zapytanie, (nazwa_ktr, typ_ktr))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Dokument '{nazwa_ktr}' o typie '{typ_ktr}' nie istnieje w bazie danych!"
    return results
    print(results)

f.time.sleep(2)

def sprawdz_art(symbol_art, rodz_art):
    zapytanie = "SELECT rodz_art, symbol_art FROM artykuly WHERE symbol_art = ? AND rodz_art = ?;"
    f.cursor.execute(zapytanie, (symbol_art, rodz_art))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Dokument '{symbol_art}' o typie '{rodz_art}' nie istnieje w bazie danych!"
    return results

def sprawdz_tech(symbol_tec, symbol_wyr):
    zapytanie = "select symbol_tec, symbol_wyr from technolog WHERE symbol_tec = ? AND symbol_wyr = ?;"
    f.cursor.execute(zapytanie, (symbol_wyr, symbol_tec))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Dokument '{symbol_wyr}' o typie '{symbol_tec}' nie istnieje w bazie danych!"
    return results

def sprawdz_poz_dok(symbol_art, ilosc, cena, klucz_dok):
    zapytanie = "select symbol_art from poz_dok where symbol_art = ? and ilosc = ?  and cena=? and klucz_dok=?;"
    f.cursor.execute(zapytanie, (symbol_art, ilosc, cena, klucz_dok))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Pozycja dokumentu '{symbol_art}'  nie istnieje w bazie danych!"
    return results

f.sprawdz_art('S1', "S")
