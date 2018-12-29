__author__ = 'dev'

# ## Continue
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         print("I am ignoring " + item)
#         continue  # skips listing spam
#     print("Buy " + item)

# ## Break
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         break
#     print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:  # else for the "for" loop in case of no break
    # nasty_food_item = '' could be defined here
    print("I'll have a plate for that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it")
