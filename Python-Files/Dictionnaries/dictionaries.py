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

# ### checking for fruit in the dictionary
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # if dict_key in fruit:
#     # fruit.has_ket(dict_key)  # Aternative of the above
#
#
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("we don't have a {}".format(dict_key))
#     description = fruit.get(dict_key, "We don't have a" + dict_key)  # does the same as the above
#     print(description)

# ### doing the iteration of the content of the dictionary
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# ### the dictionary isn't sorted in the order the information as entered, snd can change every time you load it
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' *40)

# # ordered_keys = list(fruit.keys())
# # ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))  # same as two lines above in one line
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
# # below does the same as the above in less lines
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
#
# ### values can be used too - but this is less efficient than using keys
# for val in fruit.values():
#     print(val)
#
# for key in fruit:  # much more efficient than above
#     print(fruit[key])

# ### printing all keys and all values
# print(fruit.keys())
# print(fruit.values())

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)