"""
write a program to print product of 1 to n numbers using while loop
"""


def main():
    input_number = int(input("Enter number : "))
    number = 1
    product = 1
    while number <= input_number:
        product *= number
        number += 1

    print(f'{product = }')


if __name__ == '__main__':
    main()
