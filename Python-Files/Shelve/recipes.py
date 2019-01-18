import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open('recipe') as recipes:  # before first version
with shelve.open('recipe', writeback=True) as recipes:  # for the second version

    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    ### adding elements to the recipes
    # recipes["blt"].append("butter")  # adding the content to a copy in memory, and not in the shelf
    # recipes["pasta"].append("tomato")  # so do not appear when listing from the shelf

    ### two ways of appending to the shelf
    # ## first version
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    ## second version - requires "writeback" above
    # recipes["soup"].append("crouton")
    # # issue of this method is more memory usage
    # # also writeback doesn't happen until "sync" method or shelf is closed.
    # # sync is called when the shelf is closed automatically
    # # sync moves the content from the cache to the disk, then clears the cache

    ### using Sync
    recipes["soup"] = soup
    recipes.sync()   # this caused the cache to clear, so this doesn't append
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])
