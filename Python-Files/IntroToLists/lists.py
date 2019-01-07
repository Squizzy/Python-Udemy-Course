# ipAddress = input("Please input an IP address: ")
# print(ipAddress.count("."))
parrot_list = ["not pinin'", "no more", "a stiff", "bereft of life"]

parrot_list.append("a norwegian blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
# numbers.sort()  # sort works on the existing object and doesn't create a new object so it doesn't return anything
# print(numbers)
numbers_in_order = sorted(numbers)  # sorted function creates a new object
print(numbers_in_order)

if numbers == numbers_in_order:
    print("the lists are equal")
else:
    print("the lists are not equal")

if numbers_in_order == sorted(numbers):
    print("the lists are equal")
else:
    print("the lists are not equal")
