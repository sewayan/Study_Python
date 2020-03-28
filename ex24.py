# "Stamina" exercise

print "Let's practice everything"
print 'You\'d need to know\'bout escapes with \\ that do \n newlines and \t tabs'

#-------------------
# var "poem" defined as """<- everything in between these, is the var
poem = """

\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comrpehend passion from intuition
and requires an explanation \n\twhere there is none.
"""

print "-----------"
print poem
print "-----------"

#--------------------

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#--------------------

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans /1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates, = secret_formula(start_point)

# value = 1000
print "With a starting point of: %d" % start_point
# beans = 1000 * 500 -> 500000 / 1000 etc.
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#alternative for same func, start_point = (10000 * 500) / 10
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)