
def owned_cars(cars_i_owned, cars_friends_owned):
	print "I have owned these cars: %r myself." % cars_i_owned
	print "Friends have owned these cars %r." % cars_friends_owned
	print "Wadda fack bruh\nso raaad!!"



print "What cars did you own sabbi?"
my_cars = raw_input('>')

print "And what cars did your friends own?"
friends_cars = raw_input('>')

owned_cars(my_cars, friends_cars)

	#---second part of program---
	# need to find out how to word-count the input!
print "Wanna know how many cars you guys owned in total?"
raw_input('Hit Enter')

cars_total = owned_cars

# count total no of cars, not included in function
# need to pull value from 'cars_total'...!
def car_count(cars_total):
	words = cars_total.split()
	wordCount = len(words)
print "So you owned %r cars in total" % cars_total