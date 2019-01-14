welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Cad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town waltz"))

print(imelda)
title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)
print(tracks)  # shows 4 tuples of 2 values

imelda = "More Mayhem", "Emilda May", 2011, (
    1, "Pulling the rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish town waltz")

title, artist, year, tracks = imelda
print(tracks)  # shows 1 tuple of 8 values

imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town waltz")
title, artist, year, track1, track2,  track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

imelda = "More Mayhem", "Emilda May", 2011, 1, "Pulling the rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish town waltz"

