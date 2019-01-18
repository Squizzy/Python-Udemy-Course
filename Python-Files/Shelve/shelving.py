import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = 'a sweet, orange citrus fruit'
#     fruit['apple'] = 'good for making cider'
#     fruit['lemon'] = 'a sour, yellow citrus fruit'
#     fruit['grape'] = 'a small sweet fruit growing in bunches'
#     fruit['lime'] = 'a sour, green citrus fruit'
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# # print(fruit["apple"])  # error as the file is closed when exiting "with"
#
# ### shelve can be use as a dictionary
# # but there is no literal
# print(fruit)
#
# ### You can't inisialise a shelf with literal as a dictionary

### Keeping shelf open so we can close it manual but keep using it
fruit = shelve.open('ShelfTest')
# fruit['orange'] = 'a sweet, orange citrus fruit'
# fruit['apple'] = 'good for making cider'
# fruit['lemon'] = 'a sour, yellow citrus fruit'
# fruit['grape'] = 'a small sweet fruit growing in bunches'
# fruit['lime'] = 'a sour, green citrus fruit'
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequilla"  # updating the value for a key
#
# print("=" * 40)
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
#
# print("=" * 40)
#
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     description = fruit.get(dict_key, "We don't have a " + dict_key)  # second part of get is the answer if no answer
#     print(description)
#
#     # alternative - using "in"
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("we don't have a " + dict_key)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + ": " + fruit[f])

### outputting tuples
for v in fruit.values():
    print("value: {}".format(v))

print(fruit.values())

for f in fruit.items():
    print("item: {}".format(f))

print(fruit.items())

## compared to a dictionary, a shelf key MUST be a string

fruit.close()  # Shelf must be closed manually !
