# file related exercise -> ex16.py

from sys import argv

script, input_file = argv

	#func 'print_all'-> func name, '(f)'-> file e.g. TestText.txt
def print_all(f):
	print f.read()

	#rewind file, .seek(0)-> moves file back to 0 byte
	# -> if f.seek(2) = ("Line"-> "ne") -> ?
	 # official expl. 'seek: 
	 # 0: ref point = beginning of file; (check: os.seek_set)
	 # 1: ref point = current file position; (check: os.seek_cur)
	 # 2: ref point = ref point towards end of file; (check: os.seek_end)
	
	# for second part of program
def rewind(f):
	f.seek(0)

 	# command line_count
def print_a_line(line_count, f):
		#display the result of command 'line_count' of 'f'ile
	print line_count, f.readline()

	#opens the file defined by user (e.g 'TestText.txt')
	# var 'current_file' is used with content of 'input_file'
current_file = open(input_file)


	#--- First part of Program --- 
	# displaying entire file "as-is"
print "First, let's print the whole file:\n"

print_all(current_file)


	#--- second part of program ---

print "Now let's rewind, kind of like a tape."

rewind(current_file)

	#displaying the first three lines of file 
print "Let's print three lines:"
	# displaying  text: 'Line1'

current_line = 1 # "1 Line1 "
print_a_line(current_line, current_file)

	# moving form text: 'Line1' to text: 'Line2'
#re-define 'current_line'
current_line = current_line + 1 # " 2 Line2 "-> current line defined as '1' + '1' = '2'
		# rewrite with '+='
#current_line += 1
print_a_line(current_line, current_file)


	# moving form text: 'Line2' to text: 'Line3'
#current_line = current_line + 1 # pointer moved forward in file-> current line defined as '2' + '1' = '3'
	# rewrite with '+=' -> same as x = x + y
current_line += 1 
print_a_line(current_line, current_file)