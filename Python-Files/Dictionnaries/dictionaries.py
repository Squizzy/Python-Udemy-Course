fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}  # ,
# "apple": "round and crunchy"}  # changes the value of the key defined before

# print(fruit)
# print(fruit["lemon"])
#
# # adding a dictionary entry
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# # using the same key changes the value
# fruit["lime"] = "great with tequila"
# print(fruit)
#
# # removing an entry
# del fruit["lemon"]
# print(fruit)

# delete an entire dictionary
# del fruit
# print(fruit)

# emptying a dictionary
# fruit.clear()
# print(fruit)

# reading an entry that doesn't exist causes an error
# print(fruit["tomato"])
# print(fruit)

print(fruit)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a {}".format(dict_key))