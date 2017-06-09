from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If  you do want that, hit RETURN."

raw_input("?")

print "Opening file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

final = "%s\n%s\n%s\n" % (line1, line2, line3)

target.write(final)

target.close()

print "And now let's open it. \n"
readout = open(filename, 'r')
print readout.read()

print "And finally, we close it. \n"
readout.close()
