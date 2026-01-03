age = int(input("enter your age: "))

while age < 0:
    print("age can not be negative")
    age = int(input("enter your age: "))

print(f"you are {age} years old")   