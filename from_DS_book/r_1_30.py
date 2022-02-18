"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""


def main():
    number = int(input("NUMBER : "))
    count = 0
    print(f'{number = }')
    while number > 2:
        number /= 2
        if number > 2:
            count += 1

    print(f'{count = }')


if __name__ == '__main__':
    main()
