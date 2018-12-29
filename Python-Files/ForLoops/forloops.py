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
number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("the number is{}".format(newNumber))
