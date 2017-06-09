from sys import argv
from os.path import exists

script, from_file, to_file = argv # takes script, origin and export file as inputs

print "Copying from %s to %s" % (from_file, to_file) # Just saying what's going on

# we could do these two on one line, how?
indata = open(from_file).read() # Made it shorteer, by directly reading into new var
#indata = in_file.read() #indata stores all the info in the file !!! Commented out, redundant after above line

print "The input file is %d bytes long" % len(indata) # prints out len

print "Does the output file exist? %f" % exists(to_file) # checks that an output file exists
print "Ready, hit RETURN to continue, CTRL-C to abort." # user abort option
raw_input()

out_file = open(to_file, 'w') # new variable, that stores the image of to_file
out_file.write(indata)  # puts indata into the new file

print "Alright, all done."

out_file.close() #closing up shop
