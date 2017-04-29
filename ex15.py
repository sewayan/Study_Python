
from sys import argv

	# execute script + filename
	# python ex15.py ex15_sample.txt
script, filename = argv
	#open file "txt" which has -> (name)
txt = open(filename)
	#txt = raw_input("> ") -> User input req.; error when command 'txt.read'

	# msg + content of txt file
print "Here's your file %r:" % filename

	# "txt->"calling file defined above, ".read"-> command/function/method
	# display content of txt file
print txt.read()

	#closes var txt
txt.close()

	#---second half of this program---
print "Type the filename again:"

	# user input for filename + ">" will be displayed
file_again = raw_input("> ")

	# opens file that has been defined by user input
txt_again = open(file_again)

	# displays content from file defined one line above
print txt_again.read() 

	#closes var txt_again
txt_again.close()

		#execute file in python shell e.g. "execfile ('ex5.py')"