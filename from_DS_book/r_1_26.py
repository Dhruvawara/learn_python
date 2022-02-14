"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b −c,” or “a ∗b = c
"""


def main():
    number1 = int(input("a : "))
    number2 = int(input("b : "))
    number3 = int(input("c : "))
    print('correct_arithmetic_formula({}, {}, {}) = {}'.format(
        number1, number2, number3, correct_arithmetic_formula(number1, number2, number3)))


def correct_arithmetic_formula(a, b, c):
    return True if a + b == c and a == b - c or a * b == c else False


if __name__ == '__main__':
    main()
