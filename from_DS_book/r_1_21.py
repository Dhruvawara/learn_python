"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""


def main():
    # try and except blocks are used to catch the exception
    try:
        data = input("Do you want to continue?: ")
        raise EOFError
    except EOFError:
        print("Error: No input or End Of File is reached!")
        print(data[::-1])


if __name__ == '__main__':
    main()
