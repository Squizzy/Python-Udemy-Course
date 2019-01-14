# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Cad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 1984
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)
print((metallica[0]))
print((metallica[1]))
print((metallica[2]))

# metallica[0] = "Master of puppets"  # doesn't work because you can't change a tuple
print(imelda)
imelda = imelda[0], "Imelda May", imelda[2]  # works because the RHS is evaluated first,
# a new set of objects for a tuple is created and then assigned to the previous tuple variable
print(imelda)

metallica2 = ["Ride the lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of puppets"
print(metallica2)

# Unpacking tuples
title, artist, year = imelda
print(title)
print(artist)
print(year)

# lists risks causing error in unpacking
# tuple doesn't have append method
# metallica2.append("Rock")
# title, artist, year = metallica2  # causes error

# imelda.append("Jazz")  # cannot work, you cannot append to a tuple