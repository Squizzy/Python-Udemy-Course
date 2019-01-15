### using join is more efficient

mylist = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

# newString = ''
# for c in mylist:
#         newString += c +  ', ' # not efficient as strings as immutable
#
# print(newString)

### joining items on a list
newString = ''
newString = ', '.join(mylist)

print(newString)

### joining a string
newString = ''
newString = ', '.join(letters)

print(newString)

### joining a string more complex
newString = ''
newString = ' mississippi '.join(numbers)

print(newString)

### join can be applied to disctionaries