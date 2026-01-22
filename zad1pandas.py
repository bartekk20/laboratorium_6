import pandas as pd

df = pd.read_csv("dane.csv", sep=";")
df["marża"] = (df["Sprzedaż"] - df["Koszt"]) / df["Sprzedaż"]
df = df.sort_values(by=["Rok", "Kraj"])

print(df)
