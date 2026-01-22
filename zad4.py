# Zadanie 4. Utwórz dwie tablice rozmiaru A = (2,3) oraz B = (3,2). Oblicz iloczyn skalarny tych tablic
# (A@B oraz B@A). Następnie zmień rozmiar tablicy B na (3,3). Czy mnożenia się udały? Jeżeli nie, to
# dlaczego?

import numpy as np

A = np.ones((2, 3))
B = np.ones((3, 2))

AB = A @ B
BA = B @ A

print("AB: \n", AB)
print("BA: \n", BA)

B_nowy_rozmiar = np.ones((3, 2))

try:
    AB_nowa = A @ B_nowy_rozmiar
    print("A @ B sukces", AB_nowa.shape)
except:
    print("blad 2x3 =/= 3x3 mnozenie")

try:
    BA_nowa = B_nowy_rozmiar @ A
    print("B @ A sukces", BA_nowa.shape)
except:
    print("3x3 * 2x3 blad mnozenia")

# Liczba kolumn pierwszej macierzy musi odpowiadać liczbie wierszy drugiej. Ponieważ mnożenie macierzy nie jest przemienne zmiana A@B na B@A całkowicie zmienia układ