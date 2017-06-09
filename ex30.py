people = 200
cars = 60
trucks = 40

# lines 7 - 22 are because I was annoyed with the lack of clarity in the example.


car_capacity = cars * 4
truck_capacity = trucks * 6


if car_capacity > truck_capacity:
    if car_capacity >= people:
        print "We shall take the cars."
    else:
        print "Guess we won't be going..."
elif car_capacity < truck_capacity:
    if truck_capacity >= people:
        print "We shall take the trucks."
    else:
        print "Guess we won't be going..."
else:
    print "Since the capacity is the same, let's take cars, more fuel efficient!"


# This below is the actual example

"""
if cars * 4 > people:
    print "We should take the cars."
elif cars * 4 < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

"""
