# list_1 = []
# list_2 = list()  # list constructor
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("Lists are equal")
#
# print(list("the lists are equal"))
# even = [2, 4, 6, 8]
#
# another_even = list(even)
#
# print(another_even is even)  # compares that the list are the same data
# print(another_even == even)  # compares that the content is the same
#
# another_even = sorted(even, reverse=True)
#
# print(another_even is even)  # compares that the list are the same data
# print(another_even == even)  # compares that the content is the same
#
#
# another_even.sort(reverse=True)
# print(even)
# print(another_even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print("numbers: {}".format(numbers))

for numbers_set in numbers:
    print("number_set: {}".format(numbers_set))
    for value in numbers_set:
        print("value: {}".format(value))
