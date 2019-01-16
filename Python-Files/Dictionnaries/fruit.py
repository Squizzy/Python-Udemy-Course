fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favourite",
       "sprout": "mmm, lovely",
       "spinach": "can I have more fruit, please"}

print(veg)

# veg.update(fruit)  # add the fruit dictionary to veg - update doesn't return a dictionary
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()  # make a copy without modifying the original
nice_and_nasty.update(veg)
print(nice_and_nasty)