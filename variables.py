# a variable behaves as if it was the value it contains


#strings
first_name = "kanika"
food = "ramen"


print(f"hello {first_name}")
print(f"i like to eat {food}")
print(f"{first_name} likes to eat {food}")


#integers
age = 21
num_of_students = 30
print(f"{first_name} is {age} years old")
print(f"there are {num_of_students} students in the class")


#floats
price = 10.99
print(f"the price of food is ${price}")

gpa = 3.2
print(f"your gpa is {gpa}")

# boolean

is_students = True

if is_students:
    print("you are a student")
else:
    print("you are not a student")

for_sale = False

if for_sale:
    print("the item is for sale")

else:
    print("it is not for sale")
