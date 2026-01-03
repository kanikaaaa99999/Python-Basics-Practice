#validate user input exercise
# username is no more less than 12 characters
# usermame should not contain spaces
# username should not contain digits

username = input(" Enter your name : ")
if len(username) > 12:
    print("username should be less than 12 characters")

elif not username.find(" ") == -1:
    print("username should not contain spaces")

elif not username.isalpha():
    print("username should not contain digits")


else:
    print(f"welcome {username}")