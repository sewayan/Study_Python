



print "Your height in metric system?",
height = raw_input()

print "Your weight in metric system?",
weight = raw_input()

height = ({} * 0.35 .format(height))

weight = ({} * 2 .format(weight))



# name = input("What is your name?")
# print("Hi {} let's start!".format(name)) # Will replace "{}" with name

print "Your height in the US would be %s feet, and your weight would be %s lbs" % (height, weight)