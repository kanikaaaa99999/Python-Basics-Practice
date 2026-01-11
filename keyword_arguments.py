
#keyword arguemts = an arguemts preceded by an identifier when we pass it to a function
#                    the order of the arguments does not matter , unlike positional arguments

#def hello(greeting, title, first, last):
 #   print(f"{greeting} {title} {first} {last}")

#hello( title= "ms.", first="kanika", last="sharma", greeting="hello")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=4567, last=890)
print(phone_num)