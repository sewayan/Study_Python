
from sys import argv

script, user_name, user_mood = argv
    # displays ">" when user input on command line
prompt = '>'
	# if order of argv var (below) is changed, outout is changed accordingly
print "Hi %s, I'm the %s script. Are you really %s?" % (script, user_name, user_mood)

print "I'd like to ask you a few questions."

print "Do you like me %s" % user_name

likes = raw_input(prompt)

print "Where do you live %s?" % user_name

lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How many friends do you have?"
friends = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.
Also you claim you have this number of friends %r...?!
Liar, you're a loneley wanker!
""" % (likes, lives, computer, friends)

#When you run this, remember
#that you have to give the script your name for the argv arguments.
