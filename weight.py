weight = float(input("enter your weight : "))
unit = input("klilograms or pounds ? (K/P) : ")

if unit == "K":
    weight = weight * 2.205
    unit ="lbs"
    print(f"your weight in pounds is {round(weight, 2)} lbs")
elif unit == "P":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight in kilograms is {round(weight, 2)} kg")
else:
    print(f" {unit} is invalid")