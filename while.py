# while loop ececute spme code whole condition is true

name = input("enter your name : ")

while name == "":
    print("you did not enter your name")
    name = input("enter your name : ")
    print(f"hello {name}")