

print "Your height in metric system?",
height = raw_input()

print "Your weight in metric system?",
weight = raw_input()

    #take user input and convert to imperial
height = int(raw_input())* 0.35

weight = int(raw_input())* 2



# name = input("What is your name?")
# print("Hi {} let's start!".format(name)) # Will replace "{}" with name

print "Your height in the US would be %s feet, and your weight would be %s lbs" % (height, weight)
