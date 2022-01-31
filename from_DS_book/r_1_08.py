"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤k < 0, what is the equivalent index j ≥0 such that s[j] references
the same element?
"""


def main():
    print(f'{sum_of_squares_below_if_odd(4) = }\n{sum_of_squares_below_if_odd(13) = }')
    for value in range(15):
        print(f'{sum_of_squares_below_if_odd(value) = }  \t| {value = }')


def sum_of_squares_below_if_odd(n):
    pass


if __name__ == '__main__':
    main()
