"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""


def main():
    print(f'{ sum_of_squares_below(4) = }\n{ sum_of_squares_below(13) = }')
    for value in range(15):
        print(f'{sum_of_squares_below(value) = } \t|\t {value = }')


def sum_of_squares_below(n):
    sum = 0
    for value in range(n):
        sum += (value ** 2)
    return sum


if __name__ == '__main__':
    main()
