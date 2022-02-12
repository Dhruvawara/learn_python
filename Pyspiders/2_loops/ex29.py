"""
to print product of first 10 natural numbers
"""


def main():
    product = 1
    for value in range(1, 11):
        product *= value
    print(f"{product = }")


if __name__ == '__main__':
    main()
