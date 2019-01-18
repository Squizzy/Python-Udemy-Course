import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = 'a sweet, orange citrus fruit'
#     fruit['apple'] = 'good for making cider'
#     fruit['lemon'] = 'a sour, yellow citrus fruit'
#     fruit['grape'] = 'a small sweet fruit growing in bunches'
#     fruit['lime'] = 'a sour, green citrus fruit'
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# # print(fruit["apple"])  # error as the file is closed when exiting "with"
#
# ### shelve can be use as a dictionary
# # but there is no literal
# print(fruit)
#
# ### You can't inisialise a shelf with literal as a dictionary

### Keeping shelf open so we can close it manual but keep using it
fruit = shelve.open('ShelfTest')
fruit['orange'] = 'a sweet, orange citrus fruit'
fruit['apple'] = 'good for making cider'
fruit['lemon'] = 'a sour, yellow citrus fruit'
fruit['grape'] = 'a small sweet fruit growing in bunches'
fruit['lime'] = 'a sour, green citrus fruit'

print(fruit["lemon"])
print(fruit["grape"])

fruit.close()  # Shelf must be closed manually!

