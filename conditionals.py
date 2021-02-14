# chained comparisons
number = 5
distance = 50
if 0 < number < 42 < distance:
    print("number and distance are within range")
else:
    print("number and distance are out of range!")

#the above is the same as this:
if 0 < number and number < 42 and 42 < distance:
    print("number and distance are within range")
else:
    print("number and distance are out of range!")

if 0 < number < 42 and distance != 20:
    print("number and distance are within range")
else:
    print("number and distance are out of range!")



