# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

# vowels = {"a", "e", "i", "o", "u"}
# vowels = frozenset("aeiou")
vowels = set("aeiou")

inputtext = input("Enter some text: ")

inputset = set(inputtext)

print(sorted(inputset.difference(vowels)))
