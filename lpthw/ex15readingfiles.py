# imports argv feature from sys module 
from sys import argv

# getting 2 arguments from terminal and assign to variable
script, filename = argv

# create a file object named txt for file  
txt = open(filename)

# printing text
print(f"Here's your file {filename}:")
# printing the text data
print(txt.read())
# closing the txt file object
txt.close()

# printing
print("Type the filename again:")
# geting data from user
file_again = input("> ")

# opening file
txt_again = open(file_again)

# printing file data
print(txt_again.read())
# closeing the file object
txt_again.close()