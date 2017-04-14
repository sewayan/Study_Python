     #no commas?
days = "Mon Tue Wed Thu Fri Sat Sun"
    #backslash? n? not all month?-> \n puts new line character
months = "Jan\nFeb\nMarch\nApr\nMay\nJun\nJul\nAug"

    # both outputs possible, see line 6
print   "Here are the days: %s "  % days
    #comma after string, no %s
print "Here are the months: ", months

    #neat for free text displays etc.
print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
