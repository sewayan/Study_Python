    # note the comma -> "print" will not end line with newline character
    # an go to next line

print "How old are you?",
    # tabs will result in error
age = raw_input() # let's you input data from terminal

print "How tall are you?",
height = raw_input() # raw_input -> input () in python3

print "How much do you weigh?",
weight = raw_input() # input() vs raw_input -> displays e.g. 175 instead '175'

    # displays raw dat from terminal input
print "So, you're %r old, %r tall, and %r heavy." % (
    age, height, weight)
