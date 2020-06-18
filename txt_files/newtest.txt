x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not) # 2x binary in binary

print x #print var x
print y#print var y

print "I said: %r." % x #display replica of var x # binary in binary
print "I also said: '%s'" % y #"" and '' interchangable, style/preferences # binary in binary

hilarious = False # or True  #if False = false (capitals mandatory) -> error, not defined as variable
joke_evaluation = "isn't that joke funny?! %r" # displaying replica of var

print joke_evaluation % hilarious # displays  string 'joke_evaluation' and var 'hilarious'

w = "This is the left side of..." # string w
e = "a string with a right side" # string e

print w + e # adding two stings -> longer strings
