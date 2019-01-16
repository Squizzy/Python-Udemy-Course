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


# ### subtracting set b from set a removes all the items from set b found in set a
# even = set(range(0, 40, 2))
# print("even: \t\t" + str(sorted(even)))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print("squares: \t" + str(sorted(squares)))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
#
# ### use difference_update to modify the set in place
#
# print("=" *40)
# print(sorted(even))
# print(squares)
# even.difference_update((squares))
# print(sorted(even))


# ### symmetric difference of two sets means numberd that are in one but not in the other = opposite of intersection
# even =set(range(0, 40, 2))
# print("even: \t\t" + str(sorted(even)))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print("squares: \t" + str(sorted(squares)))
#
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))


# ### removing items from sets - use discord or remove - remove will generate an error if item to be removed doesn't exist
# even = set(range(0, 40, 2))
# print("even: \t\t" + str(sorted(even)))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print("squares: \t" + str(sorted(squares)))
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # doesn't generate an error
# print(squares)
# # squares.remove(8)  # generates an error
#
# ### to use remove, make sure the item is in before
# if 8 in squares:
#     squares.remove(8)
#
# ### sometimes it is useful that there is an error
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")


# ### Testing for subset or superset - subset: all the members of a set are in the other
#
# even = set(range(0, 40, 2))
# print("even: \t\t" + str(sorted(even)))
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print("squares: \t" + str(sorted(squares)))
#
# if squares.issubset(even):
#     print("Squares in s subeet of even")
#
# if even.issuperset(squares):
#     print("even if a superset of square")

even = frozenset(range(0, 100, 2))
print(even)
even.add(3)  # doesn't work
