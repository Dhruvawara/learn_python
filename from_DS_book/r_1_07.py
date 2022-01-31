"""
Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""


def main():
    print(f'{sum_of_squares_below_if_odd(4) = }\n{sum_of_squares_below_if_odd(13) = }')
    for value in range(15):
        print(f'{sum_of_squares_below_if_odd(value) = }  \t| {value = }')


def sum_of_squares_below_if_odd(n):
    return sum([value ** 2 for value in range(n) if value % 2 != 0])


if __name__ == '__main__':
    main()
