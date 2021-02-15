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

#Sequence and collections test
mylist = []
if mylist:
    print("my list is True")
else:
    print("My List is False")

mylist = ["hello", "hi", "hey", ""]

if not all(mylist) :
    print("mylist: not all True")
if any(mylist) :
    print("mylist: at least one item is True")

#whileloops
line = None
while line != 'done':
    line = input('Type "done" to complete: ')
    print('<', line, '>')

#myl = [23, 67, 32, 77]
#while myl:
   #print(myl.pop(1))
#why is 23 1 and why is the list printed on different lines

#loop control statmement
i = 1
j = 120
while i < 120 :
    i = i * 2
    if i > j : break
else:
    print("Loop expired: ", i)
print("Final value: ", i )

#forloops
import sys
for arg in sys.argv:
    print("cmd line argument:", arg)

#countingforloops
some_list = [1, 2, 3, 4]
#for i in range(0, len(some_list)):
    #if some_list[i] > 3: some_list[i] += 1
    #print(some_list)

for i in range(0,len(some_list)) :
    print(some_list[i])
for num in some_list:
    print(num)
for idx, num in enumerate(some_list):
    if num > 42: some_list[idx] += 1
