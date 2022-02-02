"""
to perform fibonacci serires of the number
i.e starts from 0 and 1 and is addition of
previous 2 numbers using for loop.
"""


def main():
    number = int(input("Enter number : "))
    for value in range(number + 1):
        new_func(value)


def new_func(fibonacci_of):

    first_number, second_number = 0, 1
    fibonacci = 0

    if fibonacci_of < 0:
        fibonacci = fibonacci_of
    else:
        for _ in range(fibonacci_of + 1):
            fibonacci = first_number
            first_number, second_number = second_number, (
                second_number + first_number)
    print(f'fibonacci({fibonacci_of}) = {fibonacci}')


if __name__ == '__main__':
    main()
