import random as r
import numpy as np
import pygame as p
from typing import Dict, List, Tuple


def one_block(number, bo: np.ndarray) -> Tuple[np.ndarray, Dict[int, List[int]]]:
    helper = dict()
    for i in range(number):
        a = r.randint(0, 9)
        b = r.randint(0, 9)
        bo[a, b] = 1
        helper[i + 1] = [a, b]
        print(helper)

    return bo, helper


running = True
while running is True:
    ans = input('Wybierz opcję: ')
    # 1 - gra z losowanymi przez program statkami
    # 2 - gra z wybieranymi przez siebie statkami
    # add - później, gra z komputerem/ z inną osobą
    # 3 - rodzaje statków (gui/pygame)
    # 4 - ustawienia planszy
    # 5 - ranking (+ timer)
    # 6 - wyjście

    if int(ans) == 1:
        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
        s = list(range(1, 11))
        board = np.zeros((10, 10))
        traf = []
        b, h = one_block(5, board)
        print(b, h)
        print("INFO - Twoja tablica ma rozmiar 10x10, gdzie wiersz określony jest przez liczby 1-10,\
         a kolumna - przez litery A-J")
        strzal = input('Podaj pole: ')
        print(strzal)
        traf.append(letters[strzal[0]])
        traf.append(int(strzal[1]))
        if traf in h.values():
            print("Trafiony!")
        else:
            print("Pudło!")

    elif int(ans) == 2:
        print('Bye')

        running = False
    else:
        print("Wpisz poprawnie!")
