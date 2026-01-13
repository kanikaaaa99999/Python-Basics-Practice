# list comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause,
# and can also include optional if clauses to filter items.




doubles = [x * 2 for x in range(1, 11) ]
triples = [y * 3 for y in range(1, 11)]
squares = [z ** 2 for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)