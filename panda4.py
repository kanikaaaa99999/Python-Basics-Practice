#filtering is keeping the rows that meet a condition
import pandas as pd

df = pd.read_csv("data.csv")

#tall_pokemon = df[df["Height"] >= 2]
#heavy_pokemon = df[df["Weight"] >= 100]
legendary_pokemon = df[df["Legendary"] == True]
#print(tall_pokemon)        
print(legendary_pokemon)