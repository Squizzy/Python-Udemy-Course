# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.
#
locations = {0: "You are sitting in front a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of the hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# old_exits = [{"Q": 0},
#              {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#              {"N": 5, "Q": 0},
#              {"W": 1, "Q": 0},
#              {"N": 1, "W": 2, "Q": 0},
#              {"W": 2, "S": 1, "Q": 0}]

# ### First step of adding locations rather than directions
# exits = {0: {"Q": 0},
#          1: {"W": 2, "2": 2, "E": 3, "3": 3, "N": 5, "5": 5, "S": 4, "4": 4, "Q": 0},
#          2: {"N": 5, "5": 5, "Q": 0},
#          3: {"W": 1, "1": 1, "Q": 0},
#          4: {"N": 1, "1": 1, "W": 2, "2": 2, "Q": 0},
#          5: {"W": 2, "2": 2, "S": 1, "1": 1, "Q": 0}}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "3": 2},
              5: {"2": 2, "1": 1}}

keywords = {"N": "N", "NORTH": "N",
            "E": "E", "EAST": "E",
            "S": "S", "SOUTH": "S",
            "W": "W", "WEST": "W",
            "Q": "Q", "QUIT": "Q",
            "ROAD": "1",
            "HILL": "2",
            "BUILDING": "3",
            "VALLEY": "4",
            "FOREST": "5"}

# print(list(keywords.keys()))
# print(keywords.values())

### using split function

# print(locations[0].split())
# print(locations[3].split())
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    words = direction.split()
    for word in words:
        if word in keywords:
            direction = keywords[word]
            break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You can not go in that direction")
