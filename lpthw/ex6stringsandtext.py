# assigning 10 to types_of_people variable
types_of_people = 10
# assigning x with formated string "There are {types_of_people} types of people."
x = f"There are {types_of_people} types of people."

# assigning "binary" to binary variable
binary = "binary"
# assigning "don't" to do_not variable
do_not = "don't"
# assigning y with formated string "Those who know {binary} and those who {do_not}."
y = f"Those who know {binary} and those who {do_not}."

# printing x
print(x)
# printing y
print(y)

# printing formated string "I said: {x}"
print(f"I said: {x}")
# printing formated string "I also said: '{y}'"
print(f"I also said: '{y}'")

# assiging False to hilarious
hilarious = False
# assigning formatable string "Isn't that joke so funny?! {}" to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# printing joke_evaluation with hilarious with it
print(joke_evaluation.format(hilarious))

# assigning "This is the left side of..." to w variable
w = "This is the left side of..."
# assigning "a string with a right side." to e variable
e = "a string with a right side."

# printing concainated string of w and e using + operator
print(w + e)