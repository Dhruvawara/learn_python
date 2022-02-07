"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""


def main():
    print(f'{[x * (x - 1) for x in range(1,11)] =}')


if __name__ == '__main__':
    main()
