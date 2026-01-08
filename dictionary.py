
#dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values.

capitals = {"India": "New Delhi",
            "USA": "Washington DC",}

#print(help(capitals))  # to see all methods of dictionary

#print(capitals.get("japan"))

#capitals["japan"] = "Tokyo"  # adding new key:value pair
#capitals.update({"Germany": "Berlin"})  # another way to add new key:value pair
#print(capitals)

#capitals.pop("USA")  # removes the key:value pair with key "USA"
#print(capitals)
keys = capitals.keys()

for key in capitals.keys(): #same with values method like capitals.values()
    print(key)