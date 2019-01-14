# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda)

album, artist, year, tracks = imelda
print(album)
print(artist)
print(year)
for track_num, track_title in tracks:
    print(str(track_num) + "\t" + track_title)


# using list instead of tuple for the tracks
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)
imelda[3].append((5, "All for you"))

album, artist, year, tracks = imelda
imelda[3].append((6, "Eternity"))
imelda[3].append(("Bonus", "light"))

print(album)
print(artist)
print(year)
for track_num, track_title in tracks:
    print(str(track_num) + "\t" + track_title)
