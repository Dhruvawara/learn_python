"""
write a program to print sum of 1 to n natural numbers
"""


def main():
    end_number = int(input("Enter a number : "))
    number = 1
    sum = 0
    while number <= end_number:
        sum += number
        number += 1
    print(f'{sum = }')


if __name__ == '__main__':
    main()
