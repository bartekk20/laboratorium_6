# Zadanie 1. Stwórz tablicę 5x5 (wartości od 0 do 24) oraz wyciągnij z niej obramowanie (pierwszy/
# ostatni wiersz i kolumna)

import numpy as np

tablica = np.arange(25).reshape(5,5)

print("TABLICA: \n")
print(tablica)
print("KONIEC TABLICY\n")

gora = tablica[0, :]
dol = tablica[-1, :]
lewa = tablica[:, 0]
prawa = tablica[:, -1]

print("Gora: ", gora, "\nDół: ", dol, "\nLewa: ", lewa, "\nPrawa: ", prawa)

