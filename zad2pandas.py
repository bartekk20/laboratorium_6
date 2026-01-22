import pandas as pd

df = pd.read_csv("dane.csv", sep=";")
df["marża"] = (df["Sprzedaż"] - df["Koszt"]) / df["Sprzedaż"]

wynik = df[(df["Kraj"] == "DE") & (df["Rok"] >= 2023)][["Sprzedaż", "marża"]]
print(wynik)
