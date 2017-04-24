#Introduction to ' Functions'-> mini-scripts/tiny commands

#like the scripts with 'argv'
# def -> 'Define'Function, name_of_function(command e.g. *args)
# ':' (colon) needed to end line
def print_two (*args):
	#unpacks the arguments, same as scripts e.g.'argv'
	arg1, arg2 = args
	# display result
	print "arg1: %r, arg: %r" % (arg1, arg2)

#shorter version
#in python the 'unpacking' is not necessary
#arguments can be written directly into paranthesis/ 'brackets'
def print_two_again(arg1, arg2):
	print "arg1: %r, arg: %r" % (arg1, arg2)

#this jsut takes one argument else same as 'print_two_again'
def print_one(arg1):
	print "arg1: %r" % arg1

#this ones takes two arguments
def print_none():
	print "I got nothin."

print_two("Sebastian", "Wayan")
print_two_again("Sebastian", "Wayan")
print_one("First!")
print_none()

