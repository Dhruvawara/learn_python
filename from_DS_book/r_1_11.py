"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""


def main():
    print([2 ** value for value in range(9)])


if __name__ == '__main__':
    main()
