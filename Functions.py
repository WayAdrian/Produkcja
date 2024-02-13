

import pyautogui
import keyboard
import time
import pyperclip
import pytest
import sys
import datetime
import pyodbc
import datetime


pyautogui.PAUSE = 0.4


# Aktywacja okna HermesSQL
def aktywacja():
    '''

    :return:
    '''
    app_window = pyautogui.getWindowsWithTitle('humansoft HermesSQL')[0]
    app_window.activate()

# Funkcja wyswitlajaca liste okien mozliwych do aktywacji
def listaokien():
    '''

    :return:
    '''
    window_titles = pyautogui.getAllTitles()
    print(window_titles)
# klikam w wolne pole hermesa, lewy dolny róg

def data():
    '''
    :return:
    '''
    today = str(datetime.date.today())
    dzis = today.replace("-", "")
def zakladka(x):
    '''
    :param x: ilość zakładek do przejscia
    :return: przejście na kolejną zakładke
    '''
    for i in range(x):
        keyboard.press_and_release('ctrl+tab')
        time.sleep(0.2)

# loklaizacja przycisku do przekształcenia

def przeksztalc():
    '''
    :return:
    '''
    #miejsce(472,695) # laptop
    miejsce(623,-398) # serwis monitor
    #miejsce(472, 672) # mon u program




server = '10.10.10.220,2120'
database = 'Firma_CPK'
username = 'sa'
password = '3serwis4'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()


def nowytxt():
    """
    :return:  Tworzy nowy dokument .txt
    """
    with open('Raport.txt', 'w') as plik:
        sys.stdout = plik
        print(datetime.datetime.now())
        sys.stdout = sys.__stdout__



def doplikutxt(mojtext):
    """
    :param mojtext: W tym miejscu pisuje sie tekst, który zostanie dodany do pliku .txt
    :return: Dodanie treści do pliku tekstowego
    """
    with open('Raport.txt', 'a') as plik:
        sys.stdout = plik
        print(mojtext)
        sys.stdout = sys.__stdout__

def operacje(modul, dokument):
    '''
    :param modul: s- sprzedaż, z- zakupy, g- gospodarka magazynowa, k- kasa/bank,
                 r- rozrachunki, v- rejestry vat, a- analizy, p- podstawowe tabele(kartoteki),
                 o- konfiguracja, f- f administracyjne, h- ksiega handlowa,
                 i - księga przych. i rozch., a- kadry i płace HR, t- środki trwałe,

    :param dokument:
    s: d-faktura, k- korekta, w- wz, z- zwroty od klienta
    :return: Otwiera liste dokumentów
    '''
    dwa('shift', 'alt')  # otwieram operacje
    jeden('enter')
    dwa('shift', modul)
    dwa('shift',dokument)




def miejsce(a, b):
    """
    :param a: współrzędna X na monitorze
    :param b: współrzędna Y na monitorze
    :return: kliknięcie we wskazany punky
    """
    pyautogui.click(x=a, y=b)


def jeden(ten):
    """
    :param ten: oznacza nazwe klawisza klawiatury
    :return: klikniecie podanego klawisza
    """
    if ten == 'enter':
        pyautogui.hotkey('enter')  # Kliknięcie w enter
    elif ten == 'insert':
        keyboard.press_and_release('insert')
        time.sleep(1)
    elif ten == 'esc':
        keyboard.press_and_release('esc')
    elif ten == 'f12':
        pyautogui.hotkey('F12')
    elif ten == 'f5':
        keyboard.press_and_release('F5')
    elif ten == 'spacja':
        pyautogui.hotkey('space')


def dwa(pierwszy, drugi):
    """
    :param pierwszy: pierwszy klawisz
    :param drugi: drugi klawisz
    :return: klikniecie sekwencji dwóch klawiszy
    """
    pyautogui.hotkey(pierwszy, drugi)


def kilka(ile, jaki):
    """
    :param ile: ile razy kliknąć tab
    :return: kliknięcie klawisz Tab
    """
    time.sleep(0.5)
    for i in range(ile):
        keyboard.press_and_release(jaki)
        time.sleep(0.2)


def tekst(wpisz):
    """
    :param wpisz: tekst, ktory chcemy wprowadzić
    :return: wpisanie tekstu
    """
    pyautogui.write(wpisz)


def kopiowanie():
    """
    :return: kopiuje numer dokumentu i dodaje go do raportu
    """
    dwa('ctrl', 'c')

    Skopiowany = pyperclip.paste()
    numer = Skopiowany
    with open('Raport.txt', 'a') as plik:
        sys.stdout = plik
        print('Numer utworzonego dokumentu  to: ', numer)
        sys.stdout = sys.__stdout__

def zapytaniesql():
    """
    :return: Wysyła zapytanie do sql o wartość utworzonego dokumentu
    """
    x = pyperclip.paste()
    zapytanie = "SELECT KLUCZ_DOK, WARTOSC  FROM NAGL_DOK WHERE KLUCZ_DOK = '{}';".format(x)
    cursor.execute(zapytanie)
    results = cursor.fetchall()
    return results

def updatesql():
    # SQL zapytanie aktualizujące
    zapytanie = "UPDATE operacje SET aut_dok_r='1', aut_prz_p='1', aut_prz_b='1', aut_prz_o='1'"

    # Wykonaj zapytanie aktualizujące
    cursor.execute(zapytanie)

    # Zatwierdź zmiany w bazie danych
    connection.commit()


    # Zamknij kursor i połączenie





def updatesql2():
    # SQL zapytanie aktualizujące
    zapytanie = "UPDATE konf_pp SET bez_zapas = '1', prod_do_zpr = '1'"

    # Wykonaj zapytanie aktualizujące
    cursor.execute(zapytanie)

    # Zatwierdź zmiany w bazie danych
    connection.commit()


    # Zamknij kursor i połączenie
    cursor.close()
    connection.close()






def asercja(qwota):
    """
    :param qwota: wartość dokumrntu dla asercji
    :return: sprawdza czy oczekiwana wartość jest równa rzeczywistej wartości dokumentu
    oraz dodje do raportu wynik zapytania z bazy
    """
    doplikutxt(zapytaniesql())
    wynik_zapytania = zapytaniesql()
    wynik_zapytania_float = float(wynik_zapytania[0][1])
    oczekiwana_wartosc = qwota
    assert wynik_zapytania_float == oczekiwana_wartosc, "Wartość z bazy danych różni się od oczekiwanej wartości."




