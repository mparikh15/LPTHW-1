def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#turns out args is pointless, sooooo
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# limited to 1 argument
def print_one(arg1):
    print "arg1: %r" % (arg1)

#takes no arguments?
def print_none():
    print "I got nothin'."


print_two("Mayank", "Parikh")
print_two_again("Mayank", "Parikh")
print_one("First!")
print_none()
