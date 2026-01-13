
# Membership Operators in Python is used to test whether a vlue or varible is found in a senquence (string, list, tuple, set, or dictionary).
# The two membership operators are "in" and "not in".


# Example of "in" operator
word = "apple"
letter = input("guess a letter in the secret word: ")
if letter in word:
    print("correct")
else:
    print("wrong")


# Example of "not in" operator
word = "banana"
letter = input("guess a letter in the secret word: ")
if letter not in word:
    print("wrong")
else:
    print("correct")


# Example with list
fruits = ["apple", "banana", "cherry"]
fruit = input("Enter a fruit name: ")
if fruit in fruits:
    print(f"{fruit} is in the list.")
else:
    print(f"{fruit} is not in the list.")


# Example with dictionary
person = {"name": "Alice", 
          "age": 30,
          "city": "New York"}
key = input("Enter a key to check: ")
if key in person:
    print(f"{key} is present in the dictionary.")
else:
    print(f"{key} is not present in the dictionary.")

email = "kanika@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")