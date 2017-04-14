    # var 'formatter'; string with replica formatter
formatter = "%r %r %r %r"

    #print formatter = replica -> 1,2,3,4
print formatter % (1, 2, 3, 4)
    #print formatter = replica -> 'one' 'two 'three' 'four'
print formatter % ("one", "two", "three", "four")
    #python recogizes "True" & "False" as statements -> no "" or '' needed
print formatter % (True,  False, False, True)
    #displays formatter = "%r %r %r %r" as String
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    # comma after string mandatory -> Error (Syntax)
    # some string with "", some with ''-> %r displays most effectiv way
    # for debugging, not always 100% replica of typed code
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
