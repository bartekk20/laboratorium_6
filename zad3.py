# Zadanie 3. Utwórz tablice a = np.array([1, 2, 3, 4]) b = np.array([10, 20, 30, 40]). Pomnóż je element
# po elemencie oraz wyznacz iloczyn skalarny (dot product). (Wskazówka: a*b, a @ b lub np.dot(a,b))

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

mnozenie_elementow = a * b
iloczyn_skalarny = a @ b

print("Mnozenie elemtnow: ", mnozenie_elementow,
      "\nIloczyn skalarny: ", iloczyn_skalarny)