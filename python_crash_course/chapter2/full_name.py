## Chapter 2) Using variables in Strings ------------------------------------------------------------------------------
# Exercise: Want to have two separate variables for someone's name, but then create a new variable
# that displays an individuals full name.
first_name = "ada"
last_name = "lovelace"

# using 'f', which stands for format, python will then replace the variables with their values.
# python knows that the variables are variables because they are placed in curly brackets.
# this syntax reminds me of the glue function.
full_name = f"{first_name} {last_name}"
print(full_name)

# f.strings can be paired with methods to help create complex strings
print(f"Hello, {full_name.title()}!")

# without the f in-front of the " ", python prints everything out assuming that
# the information needs to be printed as written
print("Hello, {full_name.title()}!")

# rather than print out a complex f string we can assign the f strings to a variable
# to simplify the print call.
message = f"Hello, {full_name.title()}!"
print(message)

## Chapter 2) Adding whitespace to strings with tabs or newlines ------------------------------------------------------
print("Python")

# the '\t'  character combination adds a tab in front of a string.
print("\tPython")

# '\n' adds a new line to a string
print("Languages:\nPython\nC\nJavaScript")

# these two character combinations can also be used together in a single string
print("Languages:\n\tPython\n\tC\n\tJavaScript")

## Chapter 2) Stripping Whitespace ------------------------------------------------------------------------------------
# rstrip() method removes whitespace that is on the right and lstrip() removes whitespace that is on the left side of a
# string. An alternative that removes whitespace from the left and right side of a string is strip() which
# works similarly to the function trimws() in R.

# this variable is assigned a value with an extra whitespace in the end
favorite_language = 'python '

# this returns a string where the whitespace was removed, but the variable still stores a string ending with whitespace
favorite_language.rstrip()

# the white space is removed temporarily because it was not assigned to a variable that would store the information. To
# store this change permanently, you have to associate the stripped value with the variable name.
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language

# Chapter 2) Numbers --------------------------------------------------------------------------------------------------
# 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number
# 8. Be sure to enclose your operations in print() to see the results. Your output should simply be four lines with the
# the number 8 appearing once on each line.
print(6+2)
print(10-2)
print(2*4)
print(16/2)

# 2-9. Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message
# that reveals your favorite number. Print that message.
favorite_number = 2
name = "mayra"
message = f"{name.title()}'s favorite number is {favorite_number}."
print(message)
