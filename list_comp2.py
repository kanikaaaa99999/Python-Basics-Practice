
fruits = ["apple", "banana", "cherry", "date", "berry"]
fruits = [fruit.upper() for fruit in fruits ]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

numbers = [1, -2, 4, -5, -6, 8]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

neg_nums = [num for num in numbers if num < 0]
print(neg_nums)

even_nums = [num for num in numbers if num % 2 == 0] # for odd == 1
print(even_nums)
