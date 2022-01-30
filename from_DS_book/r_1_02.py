"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""


def main():
    print(f'{ even(4435) = }\n{ even(1536) = }')


def even(n):
    return True if str(n)[-1] not in '13579' else False


if __name__ == '__main__':
    main()
