"""
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""


def main():
    print(f'{ multiple(4435, 5) = }\n{ multiple(15, 3) = }')


def multiple(n, m):
    return True if n % m == 0 else False


if __name__ == '__main__':
    main()
