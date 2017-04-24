# var in functions are not connected to var in script

	# name of the function(variables-> what the funct does)
	#-> counting cheese and counting crackers;
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#display the counted cheese
	print "You have %d cheeses!" % cheese_count
	#display the counted crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#text to be displayed, \n -> creating new line
	print "DUUUDe, that's enough for a partaay"
	print "Get a blanket. \n"

	#function is displayed like above 4 times
	#below ar the 4 ways we 'called the function'

	#1st way to input 
	#-> variables 'cheese_count' &'boxes_of crackers' are fed with numbers by calling function name
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#-----

	#2nd way to input
print "OR, we can use variables from our script:"
	#define variables to use 
	#independent from function
amount_of_cheese = 10
amount_of_crackers = 50
	
	# feed variables and values into funct
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# -----

	# 3rd way to input
print "We can even do math inside too:"
	# feed funct variable directly with math
	# '10 + 20' -> cheese_count; '5 + 6' -> boxes_of_crackers
cheese_and_crackers(10 + 20, 5 + 6)


	#4th way of input
print "And we can combine the two, variables and math:"
	# value of 2nd way (cheese 10) + 100 
	# (crackers 50) + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)