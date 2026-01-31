import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

# SELECTION BY COLUMN

#print(df["Name"].to_string())   Accessing a single column
#print(df["Weight"].to_string())
# print(df[["Name", "Weight", "Height"]].to_string())  # Accessing multiple columns


# SELECTION BY ROW
print(df.iloc[0:11:2, 0:3])  # Accessing rows by integer location with step and specific columns
print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])  # Accessing rows by label range and specific columns
pokemon = input("enter a pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:    
    print("pokemon not found")