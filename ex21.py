# func can return something, no user input
	
	#func is called with two arguments 'a, b'
def add(a, b):
	#determine what arguments are doing ->'ADDING'
	# I 'add' 'a, b' &
	print "ADDING %d + %d" % (a, b)
	#return 'a, b'
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d -%d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d + %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d + %d" % (a, b)	
	return a / b


print "Let's do some math with just functions!"

	# 'var = func'
	# argumen 'add' can be assigned to any function -> e.g. 'age'
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(250, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#puzzle --- second part of program ---

print "Here is a puzzle"
	# ',' shows as '+' on command line

#-1105 <- 35 (+)	-11086	<- 74 - 11160 <- 180 + 62 <- 125/2
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"