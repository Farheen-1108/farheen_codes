# while loop:
'''  we can execute a set of statements as long as a condition is true.'''
# Print i as long as i is less than 6:
i = 1
while(i<6):
    print(i)
    i += 1     # remember to increment i, or else the loop will continue forever.

# break statement:
'''With the break statement we can stop the loop even if the while condition is true:'''
i = 1
while(i<6):
    print(i)
    if i == 3:
        break
    i = i+1

# continue statement:
''' With the continue statement we can stop the current iteration, and continue with the next: '''
i = 0
while(i<6):
    i = i + 1
    if i == 3:
        continue
    print(i)

#else statement:
'''With the else statement we can run a block of code once when the condition no longer is true:'''
i = 1
while (i<6):
    print(i)
    i = i+1
else:
    print("no longer is 6")


# for loop:
''' A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    we can execute a set of statements, once for each item in a list, tuple, set etc.
'''
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

# looping through strings:
for x in "banana":
    print(x)

# break statement:
''' we can stop the loop before it has looped through all the items: '''
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if  x == "banana":
        break
#example:
fruits = ["apple","banana","cherry"]
for x in fruits:
    if  x == "banana":
        break
    print(x)

# continue statement:
''' we can stop the current iteration of the loop, and continue with the next: '''
fruits = ["apple","banana","cherry"]
for x in fruits:
    if  x == "banana":
        continue
    print(x)

# range statement:
''' The range() function returns a sequence of numbers, starting from 0 by default, 
    and increments by 1 (by default), and ends at a specified number.'''
for i in range(6):
    print(i)

for i in range(2,6):
    print(i)

for i in range(2,30,3):
    print(i)

# else if for loop
''' The else keyword in a for loop specifies a block of code to be executed when the loop is finished:'''
for i in range(6):
    print(i)
else:
    print("successsed")

''' The else block will NOT be executed if the loop is stopped by a break statement. '''
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested Loops
''' A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":'''
adj = ["red","black","blue"]
fruits = ["apple","cherry","banana"]
for x in adj:
    for y in fruits:
        print(x,y)

# pass statements:
''' for loops cannot be empty, but if you for some reason have a for loop with no content,
     put in the pass statement to avoid getting an error.'''
for x in [1,2,3]:
    pass