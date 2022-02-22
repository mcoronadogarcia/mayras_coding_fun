# Chapter 3 --------------------------------------------------------------------
## The Basics: Example of a list that contains a few kinds of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

## Accessing Elements in a List ------------------------------------------------------------
# remember that python index positions start at 0 and not 1 like R.
print(bicycles[0])

# we can apply methods to list items
print(bicycles[0].title())

# to access the last item in a list use -1. The index -2 returns the second item from the
# end and -3 returns the third item from the end, etc
print(bicycles[-1].title())

## Using individual values from a list -----------------------------------------------------
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

## Changing, Adding, and Removing Elements -------------------------------------------------
# to change a value in a list, call the list and the location of the old value you want to
# change, then set that indexed value equal to the desired value
print(bicycles)
bicycles[0] = "new bicycle"
print(bicycles)

# there are several ways to add an element to a list.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# you can use append a list that already has items.
bicycles.append('new bicycle')
print(bicycles)

# you can also append an empty list
bicycles2 = []
bicycles2.append('trek')
bicycles2.append('cannondale')
bicycles2.append('redline')
bicycles2.append('specialized')
bicycles2.append('new bicycle')
print(bicycles2)

# you can insert values in any place is a list using insert()
bicycles_using_insert = ['trek', 'cannondale', 'redline', 'specialized']
print("starting list", bicycles_using_insert)

bicycles_using_insert.insert(0, "new bike")
print("updated list", bicycles_using_insert)

# remove elements from a list using the del statement
bicycles_using_del = ['trek', 'cannondale', 'redline', 'specialized']
print("starting list", bicycles_using_del)

del bicycles_using_del[0]
print("updated list", bicycles_using_del)

# removing an item using the pop() method
# this method is used when you need to delete an item, but still need to access their
# information.
bicycles_using_pop = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles_using_pop)

# by using pop(), bicycles last item will be removed and the new
# list popped_bicycles will have the item that was removed.
popped_bicycles = bicycles_using_pop.pop()
print(bicycles_using_pop)
print(popped_bicycles)

# when would it be useful to keep the last item? Useful when there is an
# order to a list. For example, figuring out last purchased motorcycle.
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# if a list doesn't have an order, you can still use pop to access
# an item after removing it from a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# you can also remove an item by value using the remove method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# note that remove() only removes the first occurrence of a method.
# if you need to remove a couple items with the same value, then use a loop.
motorcycles.remove('yamaha')
print(motorcycles)

## Organizing a List -----------------------------------------------------------------------
# sort() and reverse() permanently order a list. to display a sorted list, but keep the order
# use sorted(). You can also set sort() to use a reverse = TRUE argument.
