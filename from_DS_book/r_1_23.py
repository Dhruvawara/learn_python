"""
Give an example of a Python code fragment that attempts to write an element 
to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""


def main():
    list_variable = []
    try:
        list_variable[0]
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")


if __name__ == '__main__':
    main()
