# __author__ = 'dev'
# for i in range(1,20):
#     print("i is now {}".format(i))
#
# number = "9,223,372,036,854,775,807"
#
# for i in range(0,len(number)):
#     print(number[i])

# number = "9,223,372,036,854,775,807"
#
# for i in range(0,len(number)):
#     if number[i] in '0123456789:':
#         print(number[i])


# number = "9,223,372,036,854,775,807"
#
# for i in range(0,len(number)):
#     if number[i] in '0123456789:':
#         print(number[i],end='')  #  Override the new line

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for i in range(0,len(number)):
#     if number[i] in '0123456789:':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)   #  convert string to int
# print("the number is{}".format(newNumber))

####  Extending for loops
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("the number is{}".format(newNumber))


# for state in ["not pinin'", "no more", "a stiff", "bereft of life", ]:
#     print("This parrot is " + state)
#     #  peint(This parrot is {}".format(state))  # can be used as well

# for i in range(0,100,5):
#     print("i is {}".format(i))

### nested loops
# for i in range(1, 13):
#     for j in range(1, 13):
#         print("{1:2} times {0:2} is {2:3}".format(i, j, i*j), end="\t")
#     print('')


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

###  Exercises

# Use a for loop and an if statement to print just the capitals in the quote above.
newQuote = ''

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        newQuote = newQuote + char
print(newQuote)

for i in range(0,101):
    if i/7 == i//7:
        print(i)