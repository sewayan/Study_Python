    #\t to create a tab (space)from the start of line
tabby_cat = "\tI'am tabbed in."
    #\n new line character, "on a line" in next line
persian_cat = "I'm split\non a line."
    # displays-> I'm \ a \ cat
backslash_cat = "I'm \\ a \\ cat."
    # 'Boooyah' displayed below, after line-break
realest = "100 %\nBoooyah"

    # creates a tab, '*' -> displayed in string
    # ''' instead of """ -> preferences
fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
 """
 # %r vs %s
 # %r -> I luuuv them naptime, keepin it '100 %'
 # %s -> I luuuv them naptime, keepin it 100 %
fat_cat_fatso = "I luuuv them naptime, keepin it %s" % realest

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat_fatso
