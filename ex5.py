name = "SabbiPooh the Wayan"

age = 34 #only one value for one variable (e.g. string or int)
            # not e.g. age= "forever21", 34
weight = 80 # kg
weight_pound = weight * 2.20462262 #if you want to round -> round (2.20462262)
height = 179 # cm
height_feet = height / 0.03
eyes = "brown"
teeth = "white"
hair = "black"
no_matter_what = "boobies!"

print "Let's talk about %s" % name #no comma possible after string, %s formatter for string
print "He's %d cm tall." % height # %d formatter for integer 
print "He's %d kg heavy" % weight
print "Good weight"
print "He's got %s eyes and %s hair"  % (eyes, hair) #mult. var in brackets
print "His teeth are usually %s depending on the amount of coffee he is drinking" % teeth

print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

print "My weight in pound is %d pound" % weight_pound
print "My height in the imperial measurement system is %d feet" % height_feet

print "My weight no matter what %r" % no_matter_what # %r will print the whole string
# including "" or ()