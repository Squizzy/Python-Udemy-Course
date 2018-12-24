__author__ = 'dev'
# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Please enter your name: ")
age = int(input("Hi {}, good to meet you. please enter your age".format(name)))

# if 18 <= age < 31:
if (age >= 18) and (age < 31):
    print("Welcome to the 18-30 holiday")
else:
    print("I'm sorry, this a 18 to 30 holiday club exclusively")

# not age:
# print("You must enter your age")
# elif