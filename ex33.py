numbers = []
limit = 12
step_counter = 1

# study drill 5
for i in range (0,12):
    print "At the top i is %d" % i
    numbers.append(i)
    i += step_counter
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

# study drills 1, 2, 3, 4

"""def while_loop (limit):
    i = 0
    while i <= limit:
        print "At the top i is %d" % i
        numbers.append(i)
        i += step_counter
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

while_loop(limit) """

# original

"""while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i"""

print "The numbers: "

for num in numbers:
    print num
