import shelve

books = shelve.open("book")

### using dictionaries only
# books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
#                      "beans_on_toast": ["beans", "bread"],
#                      "scrambled eggs": ["eggs", "butter", "milk"],
#                      "soup": ["tin of soup"],
#                      "pasta": ["pasta", "cheese"]},
#          "maintenance": {"stuck": ["oil"],
#                          "loose": ["gaffer tape"]}}

### dictoniaries from above modified for shelves
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                       "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])
print(books["maintenance"]["loose"])

books.close
