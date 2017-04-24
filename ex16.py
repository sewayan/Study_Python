
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename

print "If you don't want that, hit CONTROL-C."

print "If you do want that, hit ENTER"

	#displays "?"in a seperate line
raw_input("?")

print "Opening the file..."
	# 'w'-> modifier; writing 
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
	# opening in 'w' already wiped the file
	# if file is opened w/o modifier, truncate can e.g. delete partial
target.truncate()
    # @this point "test.txt"-> empty

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'am going to write these to the file."

	#write line1, write a new line "\n", write line2
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

	#one line, same function as line 34 -39
	# concatenate with '+'
	# line1 -> var, no ""
	# "\n" -> command, needs ''
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

	#open file after 'write'
target = open(filename)
	# display content of file 'filename'-> input by user
print target.read()

print "And finally, we close it"
	#closing the file
target.close()

    #test.txt has been made manually for program to write in
	# a file can be created from terminal -> provide filename as 2nd argument    
