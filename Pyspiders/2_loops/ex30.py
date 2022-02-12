"""
to perform factorial of an given number
"""


def main():
    factorial = 1
    factorial_of = int(input("Enter number : "))
    if factorial_of == 0:
        factorial = 1
    for value in range(1, factorial_of + 1):
        factorial *= value

    print(f'{factorial = }')


if __name__ == '__main__':
    main()
