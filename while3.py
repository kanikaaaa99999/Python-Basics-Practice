food = input("enter food you like (q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit): ")
print("bye")