# ### 2 ways to create sets
#
# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])  # literal is { }
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
#
#
# ### cannot create an empty set with curly brackets, it would create a dictionary
#
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# #empty_set2.add("a")  # doesn't work - can't "add" to a dictionary
#
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)


# ### Using union to combine without replicating
# even = set(range(0,40,2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
#
# ### intersextion identifies the items that are common
# print("-" *40)
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)


### subtracting set b from set a removes all the items from set b found in set a
even = set(range(0,40,2))
print("even: \t\t" + str(sorted(even)))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("squares: \t" + str(sorted(squares)))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even-squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)