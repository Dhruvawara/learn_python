'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''


def main():
    print(f'{sum_of_squares_below_if_odd(4) = }\n{sum_of_squares_below_if_odd(13) = }')
    for value in range(15):
        print(f'{sum_of_squares_below_if_odd(value) = }  \t| {value = }')


def sum_of_squares_below_if_odd(n):
    sum_of = 0
    for value in range(n):
        if value % 2 != 0:
            sum_of += (value ** 2)
    return sum_of


if __name__ == '__main__':
    main()
