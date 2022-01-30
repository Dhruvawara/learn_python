"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def main():
    data1 = [1534, 3545, 456, 468, 765, 4, 5456, 74,
             654, 654, 564, 54, 54, 3541, 543, 54653, 4, ]
    data2 = [49864567, 8798, 464, 489674, 8634,
             8546, 3418674865, 34, 46, 7465, 486, 74684, ]
    print(f'{minmax(data1) = }\n{minmax(data2) = }')


def max_(data):
    max_number = 0
    for value in data:
        if value > max_number:
            max_number = value
    return max_number


def min_(data):
    min_number = 999999999999999999
    for value in data:
        if value < min_number:
            min_number = value
    return min_number


def minmax(data):
    return max_(data), min_(data)


if __name__ == '__main__':
    main()
