# Find python codes (e.g. on github) and read it
# find out what it does
# identify the parts of the code and comment

	#func 'get_user_input'
    #-> iput is limited to input>6 or input<1
def get_user_input(start,end):
	# '='-> assign value to var, in this case value = statement
    testcase = False
    # '==' -> equality operator
    # comparing var with value -> is var "testcase" "False"?
    while testcase == False:
    #-> iput is limited to input>6 or input<1
        try:
    #int-> input for integer (Python3); like raw_input in python2 -> returns just strings
    # -> need to convert with "int"-> see float(raw_input())?
            userInput = int(input("Enter Your choice: "))
    #condition for "testcase = false"
    # messag is displayed if condition is met -> input is not in defined range
            if userInput > 6 or userInput < 1:
                print("Please try again.")
                testcase = False
    #if input is in defined range, the input is displayed
            else:
                return userInput
    # if input is e.g. string, error msg is displayed
    #-> getting syntax error?   
        except ValueError:
            print("Please try again.") 
        
    # var for display, get user input(has to be in rang of 1 - 6)
    # print var 'x'
x = get_user_input(1,6)
print(x)