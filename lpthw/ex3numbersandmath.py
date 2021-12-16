# + : plus                  -> Addtion
# - : minus                 -> Subtraction
# / : slash                 -> Division
# * : asterisk              -> Multiplication
# % : percent               -> Modulus
# < : less-than             -> Comparision Operator
# > : greater-than          -> Comparision Operator
# <= : less-than-equal      -> Comparision Operator
# >= : greater-than-equal   -> Comparision Operator

# PEDMAS
# P  Parentheses, then
# E  Exponents, then
# MD Multiplication and division, left to right, then
# AS Addition and Subtraction, left to right

#  Evaluation of expressions is done from left to right

# printing "I will now count my chickens:"
print("I will now count my chickens:")

# printting "Hens:" and 25 + 30 / 6 expression value
print("Hens:", 25 + 30 / 6)  # (30 / 6)5.0 + 25 = 30.0
# printting "Roosters:" and 100 - 25 * 3 % 4 expression value
print("Roosters:", 100 - 25 * 3 % 4)  # 100 - 3(75(25 * 3) % 4) = 97

# printing "Now I will count the eggs:"
print("Now I will count the eggs:")

# printing 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 expression value
print(
    3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
)  # 3 + 2 + 1 - 5 + 0(4 % 2) - 0.25(1 / 4) + 6 = 6.75

# printing "Is it true that 3 + 2 < 5 -7?"
print("Is it true that 3 + 2 < 5 -7?")

# printing 3 + 2 < 5 - 7 expression value
print(3 + 2 < 5 - 7)  # False

# printing "What is 3 + 2?" and 3 + 2 expression value
print("What is 3 + 2?", 3 + 2)  # 5
# printing "What is 5 - 7?" and 5-7 expression value
print("What is 5 -7?", 5 - 7)  # -2

# printing "Oh, that's why it's False"
print("Oh, that's why it's False")

# printing "How about some more."
print("How about some more.")

# printing "Is it greater?" and 5 > -2 expression value
print("Is it greater?", 5 > -2)  # True
# printing "Is it greater or equal?"and 5 >= -2 expression value
print("Is it greater or equal?", 5 >= -2)  # True
# printing "Is it less or equal?" and 5 <= -2 expression value
print("Is it less or equal?", 5 <= -2)  # False