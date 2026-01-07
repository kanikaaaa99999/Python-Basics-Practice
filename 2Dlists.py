
   
groceries = [("apple", "banana", "cherry"),
             ("carrot", "broccoli", "spinach"),
             ("chicken", "beef", "pork")    ]


for collection in groceries: 
   for food in collection:
      print(food , end=" ")
   print()  # for a new line after each collection