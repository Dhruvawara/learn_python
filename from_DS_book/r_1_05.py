"""
Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function
"""


def main():
    print(f'{sum_of_squares_below(4) = }\n{sum_of_squares_below(13) = }')
    for value in range(15):
        print(f'{sum_of_squares_below(value) = } \t| {value = }')


def sum_of_squares_below(n):
    return sum([value ** 2 for value in range(n)])


if __name__ == '__main__':
    main()
