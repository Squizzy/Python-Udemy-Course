import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "red"
    # bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["engin_size"])  # the entry has remained after the correction of the entry of the key
    print(bike["colour"])

### shelves are persistent

### type with typo, then run again with without typo
# bike["engin_size"] = 250

# can interate through the kets
    for key in bike:
        print(key)

    del bike['engin_size']  # easy to remove unneeded entries

    for key in bike:
        print(key)
