# Zadanie 2. Dla macierzy losowej 6×4 (N(0,1)) znajdź: średnią każdej kolumny, indeksy min/max w
# każdej kolumnie
import numpy as np

rand_macierz = np.random.rand(6, 4)

print(rand_macierz, "\n")

srednia_kazdej_kolumny = np.mean(rand_macierz, axis=0)

indeks_min = np.argmin(rand_macierz, axis=0)

indeks_max = np.argmax(rand_macierz, axis=0)

print("Srenida kolumn: ", srednia_kazdej_kolumny,
      "\nMin: ", indeks_min,
      "\nMax: ", indeks_max)