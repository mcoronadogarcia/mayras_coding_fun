# simple example ----------------------------------------------------------
# The overall format is similar to how to write an if statement in r,
# main difference is the exclusion of () and {}
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for inequality -------------------------------------------------
# an exclamation point infront of the equal size represents not.
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")
