# Looping Through an Entire List -------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# this for loop is basically saying "For every magician in the list of magicians, print the
# magician’s name."

# A closer look at looping -------------------------------------------------------------------------
# Using singular and plural names can help you identify whether a section of code is working with a
# single element from the list or the entire list.

# Doing More Work Within a For Loop ----------------------------------------------------------------
# each line indented after the for loop statement is initiated, is inside the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# if we want to say an additional comment to each person then we just add a line after the initial
# print statement
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing Something After a for Loop -----------------------------------------------------------------
# any lines of code after the for loop that is not indented are executed once without repetition.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Avoiding Indentation Errors ----------------------------------------------------------------------
# pythons use of indentations make it easy to read since it uses white space to force you to write
# neatly formatted code with a clear visual structure.

# In longer scripts you'll notice blocks of indented  code in different levels. These indentation
# levels help you gain a general sense the programs overall organization.

# common indentation errors
# - Forgetting to Indent: When python expects an indented block and it doesn't find one, it lets
#   you know.
# - Forgetting to Indent Additional Lines (Logical Error): No error is given, but results are
#   incorrect
# - Indenting Unnecessarily: Python lets you know about unexpected indents.
# - Indenting Unnecessarily After the Loop (logical error): This will cause the line to be repeated for each item
#   in a loop.
# - Forgetting the Colon: A syntax error is returned because python doesn't understand what you are
#   doing.

# Making Numerical Lists ----------------------------------------------------------------------------
# The range function makes it easy to generate a series of numbers.
print("\nRange from 1 to 5 gives you: ")
for value in range(1, 5):
    print(value)
# note that range from 1 to 5 does not give you 5. This is because of the off by one behavior in
# python. Python starts counting at the first value you give it, but it stops when it reaches the
# second value, the output never contains the end value.

print("\nIf you provide the range function one value, the list starts at 0.")
for value in range(6):
    print(value)

# if you want to make a list of numbers, you can make a list by calling the range function
# and wrapping list() around it.
numbers = list(range(1, 6))
print("\nStore a range of numbers in a variable using a list: ", numbers)

# we can skip values from numbers in a range by providing a third argument which is a step size
# basically what this does is it starts at 2 and add 2 until it reaches or passes the end value.
# in this case it is 11.
even_numbers = list(range(2, 11, 2))
print("\nA list of numbers from 2 to 11 and using 2 as a step argument:", even_numbers)
# note that here we would reach 11, but because of the one off nature of python, we don't end on
# the last value.
even_numbers2 = list(range(1, 11, 2))
print("\nA list of numbers from 1 to 11 and using 2 as a step argument:", even_numbers2)

# If we were trying to get the square of the numbers from 1 to 10, then we would
# create a range from 1 to 11 and in a for loop square each number and store their information

print("\nCreate a list of the first 10 square numbers")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# another way of doing this is to omit the temp variable. Note that sometimes using temp variables
# makes your code easier to read and other times might make your code unnecessarily long.
print("\nCreate a list of the first 10 square numbers without a temp variable.")
squares2 = []
for value in range(1, 11):
    squares2.append(value**2)

print(squares2)

# using min(), max(), and sum() function, you can calculate a couple summary stats for a list
# of digits.
digits = list(range(1, 10))
digits.append(0)
print("\nThe following summary statistics are for the following list of values: ", digits)
print("Min:", min(digits))
print("Max:", max(digits))
print("Sum:", sum(digits))

# list comprehension example
squares3 = [value**2 for value in range(1, 11)]
print("\nThe following list is generated using list comphrension ('squares3 = [value**2 for value in range(1,11)]'): ", squares3)

# to access a subsection of values in a list, you will slice them.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nOriginal player list and order:",
      players)

print("\nBy using a index from 0 to 3, we are asking for the first, second, and third players in a list:",
      players[0:3])

print("\nBy omiting the first number we are asking for the first to the fourth players in a list:",
      players[:4])

print("\nBy omiting the last number we are asking for the third to the last players in a list:",
      players[2:])

print("\nBy using a negative 3 as the first value in the index, you get the last 3 items in a list:",
      players[-3:])

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# making a copy of an exisiting list. You do this by accessing all items in a list by not telling
# python the start of end of a slice. it assumes then the slice is from the first to the last
# item in a list.
my_foods = ['pizza', 'falafel', 'carrot cake']

# friend_foods = my_foods # note this is wrong since any changes to the origianl variable will impact
# this new variable.
friend_foods = my_foods[:]

# add new food two each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# making tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# An error is given when we try to change the value of an item in a tuple.
# dimensions[0] = 250
# print(dimensions[0])

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
       print(dimension)

# Styling Your Code ---------------------------------------------------------------------------------