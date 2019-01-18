# import turtle  # used before selecting to import specific functions
# # import time  # used to add the sleep time at the end of the program, before using "turtle.done()"
#
# # noinspection PyUnresolvedReferences
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
# turtle.done()
#
# # time.sleep(4)

# from turtle import forward, right, done
# import turtle
#
# forward(150)
# right(250)
# forward(150)
# turtle.circle(75) # doesn't work as module turtle is not imported (when line 13 is not there
# # circle(75)  # doesn't work as circle is not imported
# done()

# ### alternative
# from turtle import *  # not preferred as may import functions we don't know
#
# forward(150)
# right(250)
# forward(150)
# circle(75)
# done()

### alternative
# example of why importing * is not good
# done = "Well done, you have finished the drawing"

from turtle import *  # not preferred as may import functions we don't know

done = "Well done, you have finished the drawing"

forward(150)
right(250)
forward(150)
circle(75)
done()

print(done)