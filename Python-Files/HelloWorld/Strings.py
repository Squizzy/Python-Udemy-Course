# Strings are Sequence Data Types

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[0])
# print(parrot[14]) # Out of Range
print(parrot[-1])
print(parrot[0:6]) # first postition:number of chars
print(parrot[3:5])
print(parrot[:6])
print(parrot[7:])
print(parrot[-4:2]) # doesn't work, because can't go forward from beginning of string
print(parrot[-4:-2])
print(parrot[0:6:2]) # jumps in steps
print(parrot[0:6:3]) # increment step of 3

number = "0,223,372,036,854,775,807"
print(number[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

string1 = "he'S "
string2 = "probably "
print(string1+string2)
print("he's " "probably " "pining ")
print("Hello " *5)
#print("Hello " *5 +4) # fails
print("Hello " *(5 +4))
print("Hello " *5 + "4")

today = "Friday"
print("day" in today)
print("fri" in today)
print("Fri" in today)
print("Thur" in today)
print("parrot" in "fjord")
print("parrot" in "Fjordian parroticus")