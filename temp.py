unit = input("is this temperature in celsius or fahrenheit (C/F): ")
temperature = float(input("enter the temperature : "))

if unit == "C":
    temperature = round((temperature * 9) /5 +32 , 1)
    print(f"the temperature in fahrenheit iis : {temperature} F")

elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9 , 1)
    print(f"the temperature in celsius is : {temperature} C")

else:
    print(f"{unit} is invalid")
