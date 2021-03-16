fruits = []

vegetables = ["Carrots", "Peas"]
#print(vegetables)

# adding items to a list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomato")
# to show how .remove works. As this removes only the first occurance of banana
fruits.append("Banana")
# append adds to the list, to the end of the list
print(fruits)

# removing items from a list
fruits.remove("Banana")
print(fruits)

# remove items by index
del fruits[1]
print(fruits)

# insert a value but not at the end. As append adds at the end.
fruits.insert(1, "Pineapple")
print(fruits)

# access a item from a list using index.
print(fruits[0])
