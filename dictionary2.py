
#consession stand program

menu = {"pizza": 10.00,
        "burger": 7.00,
        "fries": 12.00,
        "soda": 5.50,
        "salad": 8.00,
        "hotdog": 6.00,
        "ice cream": 4.50,
        "popcorn": 3.00}

cart =[]
total = 0

print("Welcome to the Concession Stand!")
print("-------------MENU-------------")
for key , value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----------CART ITEMS-----------")      
for food in cart:
    total += menu.get(food)
    print(food, end=" ")    


print()
print(f"your total is : ${total:.2f}")