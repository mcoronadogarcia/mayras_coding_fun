# Chapter 2) Strings Section
# the following line assigns the value "ada lovelace" to the variable 'name'
name = "ada lovelace"

# this print statement, prints the variable 'name' and capitalizes the first letter of each word
# in the string like a title because of the method .title(). The dot before the method title()
# tells python to act on the variable 'name'
print(name.title())

# The method title() will take a string with an array of capitalization's and output the return value
# with the first letter of each word capitalized.
name = "Ada"
print(name.title())

name = "ADA"
print(name.title())

name = "ada"
print(name.title())

name = "aDa"
print(name.title())

# there are many other useful methods.
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
