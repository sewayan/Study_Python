# exercise for ex21.py

def add(a, b):
	print "Iam adding %d + %d" % (a, b)
	return a + b

# 'raw_input'does not work-> can't enter "floating point"-> fixed str or int needed
# 'float'-> int can be input by user,no str possible
a = float(raw_input('>'))
b = float(raw_input('>'))

result = a + b

print "Your result is %d" % result

# example input '$2' & '$1' -> '21' not '3' -> "%r"!!!
# if "%d" -> integer needed not string