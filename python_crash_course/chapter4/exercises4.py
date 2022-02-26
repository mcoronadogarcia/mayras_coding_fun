# Chapter 4-1. Pizzas -------------------------------------------------------------------------------
pizzas = ["pepperoni", "bacon", "cheese"]

for pizza_type in pizzas:
    print(f"I like {pizza_type} pizza.\n")

print("I really love pizza!")

# Chapter 4-2. Animals ------------------------------------------------------------------------------
animals = ["dog", "cat", "hamster", "bird"]

for animal in animals:
    print(f"A {animal} would make a great pet.\n")

print("Any of these animals would make a great pet!")

# Chapter 4-3. Counting to Twenty -------------------------------------------------------------------
for value in range(1, 21):
    print(value)

# Chapter 4-4. One Million --------------------------------------------------------------------------
millions = list(range(1, 1000001))
print(millions)

# Chapter 4-5. Summing a Million --------------------------------------------------------------------
print("Min:", min(millions))
print("Max:", max(millions))
print("Sum:", sum(millions))

# Chapter 4-6. Odd Numbers --------------------------------------------------------------------------
odd_numbers = list(range(1, 20, 2))
print("\nPrint a list of odd numbers")
for number in odd_numbers:
    print(number)

# Chapter 4-7. Threes -------------------------------------------------------------------------------
multiples_of_three = [value*3 for value in range(1, 11)]
for number in multiples_of_three:
    print(number)

# Chapter 4-8. Cubes --------------------------------------------------------------------------------
cubes = [value**3 for value in range(1, 11)]

for number in cubes:
    print(number)

# Chapter 4-9. Cube Comprehension -------------------------------------------------------------------
cubes = [value**3 for value in range(1, 11)]

for number in cubes:
    print(number)

# Chapter 4-10. Slices ------------------------------------------------------------------------------
cubes = [value**3 for value in range(1, 12)]
print("\nOriginal list:", cubes)
print("\nThe first three items in the list are:\n")

for cube in cubes[:3]:
    print(cube)

import math

print("Three items from the middle of the list are:\n")

middle_index = math.ceil(len(cubes)/2)
middle_start = middle_index - 2
middle_end = middle_index + 1

for cube in cubes[middle_start:middle_end]:
    print(cube)

print("The last three values are:\n")

for cube in cubes[-3:]:
    print(cube)

# Chapter 4-11. My pizzas, your pizzas --------------------------------------------------------------
pizzas = ["pepperoni", "bacon", "cheese"]
friends_pizzas = pizzas[:]

pizzas.append("jalapeno & pepperoni")
friends_pizzas.append("bbq chicken")

print("\nMy favorite pizzas are:")

for pizza_type in pizzas:
    print(pizza_type)

print("\nMy friend's favorite pizzas are:")

for pizza_type in friends_pizzas:
    print(pizza_type)

# Chapter 4-13. Buffet ------------------------------------------------------------------------------
foods = ("taco", "flauta", "pupusa", "caldo", "sopes")

print("\nThis restaurants food includes:")
for food in foods:
    print(food)

foods = ("taco", "flauta", "pupusa", "menudo", "caldo de res", "sopes")

print("\nThis restaurants food was redesigned and now includes:")
for food in foods:
    print(food)
