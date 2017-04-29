
	#write in one line with ';' as seperation -> ',' = error
					# module/script/library for 'exists - boolean'
from sys import argv; from os.path import exists

	
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

	# write this in one line -> seperate with ';'
	# opens file defined by user -> data is assigned to 'in_file'
	# in_file is read and becomes 'indata'
in_file = open(from_file); indata = in_file.read()
	

	#old length check + 'exist boolean'	
#print "The input file is %d bytes long" % len(indata)
#print "Does the output file exist? %r" % exists(to_file)

 
	#length check + boolean to check file is existing
print "The input file is %d bytes long\nand the output file exists? %r" % (len(indata), exists(to_file))


#print "Ready, hit RETURN to continue, CTRL-C to abort" -> unnecessary feature
	
	# User input "execute or abort"
#raw_input()  -> unnecessary, if put in, user needs to hit ENTER or CMD-C


	# open file in 'write'
							# write data in file
	# can be written in one line by ';' seperation -> ',' = error
out_file = open(to_file,'w'); out_file.write(indata)

	
print "Alright, all done."

	# write this in one line -> seperate with ";"
out_file.close(); in_file.close()

# _file.close() -> needed bc Python does not promis to close file
# => run out of ressource if program continues longer after file is used
# => files might not be allowed to be 'open' in 'write' & 'readonly' simultaniously
# -> close files after use, reopen if needed (e.g. with different 'mode')	
 	# create file in command line " $echo 'File content (e.g. a text)'  > filename.filetype"
	# comand line "cat + filename"-> content of file as string
