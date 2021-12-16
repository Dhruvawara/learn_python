from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv #if less or more values are given it throws ValueError

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variabl is:", third)
# 3 -> use input
number=int(input("Enter a number:"))
print(number)

# modules gives us freatures