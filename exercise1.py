# shopping cart

item = input("what item would you like to buy?: ")
price = float(input("what is the price?: ")) 
qunatity = int(input("how many would you like to buy?: "))
total = price * qunatity

print(f"you have bought {qunatity} x {item}/s")
print(f"your total is: ${total}")