# A variable is nothing more than a name for something

# cars variable is initialized to 100
cars = 100
# space_in_a_car variable is initialized to 4.0
space_in_a_car = 4.0
# drivers variable is initialized to 30
drivers = 30
# passengers variable is initialized to 90
passengers = 90
# cars_not_driven variable is initialized to cars - drivers
cars_not_driven = cars - drivers
# cars_driven variable is initialized to  drivers
cars_driven = drivers
# carpool_capacity variable is initialized to cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car variable is initialized to passengers / cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are {0} cars available.".format(cars))
print("There are only", drivers, "drivers available.")
print(
    "there will be ", cars_not_driven, " empty cars today."
)  # Will put an extra space
print("We can transport %s people today." % carpool_capacity)
print("We have %s to carpool today." % passengers)
print("We need to put about {} in each car".format(average_passengers_per_car))

# When variable is used but not defined before then we will get NameError
# 1-> When in space_in_a_car is given the value 4 instead of 4.0 then the carpool_capacity variable will have integer value

# Single-equal(=) assigns the value to the right to a variable on the left
# double-equal(==) checks whether two things have same value
