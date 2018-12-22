__author__ = 'dev'

age = 24
# print("mMy age is " + age + " years old")

print("My age is " + str(age) + " years")

# Replacement Fields
print("My age is {0} years".format(age))

# New in python 3
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "Januarry", "March", "May", "July", "August", "October", "December"))

print("""January: {2},
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31))

# deprecated in python 3
print("My age is %d years" % age)

print("my age is %d %s %d %s" % (24, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squired is %4d and cubed is %4d" % (i, i**2, i**3))  # +2d means use 2 chars for spacing

print("Pi is approximately %12.50f" % (22/7))
# End of deprecated

