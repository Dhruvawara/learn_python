"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""


def main():
    print(f'{[chr(x) for x in range(97,123)] = }')


if __name__ == '__main__':
    main()
