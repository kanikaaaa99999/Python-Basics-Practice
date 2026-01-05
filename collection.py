#collection = single variable used tostore multiple values
# list [] , tuple () , set {} , dictionary {key:value}
#list = ordered , changeable , allows duplicate values
#set = unordered , unindexed , no duplicate values
#tuple = ordered , unchangeable , allows duplicate values faster than list
#dictionary = unordered , changeable , indexed , no duplicate keys



fruits = ["apple", "banana", "mango", "grapes" , "orange" , "kiwi"]
#print(fruits[::2])

#for fruit in fruits:
 #   print(fruit)
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print ("pineapple" in fruits)
#fruits[0] ="pineapple"
#for fruit in fruits:
     #print(fruit)

#fruits.append("pineapple")
#print(fruits)
#fruits.remove("apple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("mango"))