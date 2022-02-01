"""
to perform sum of first 10 natural numbers
"""


def main():
    sum = 0
    for value in range(10):
        sum += value
    print(f"{sum = }")


if __name__ == '__main__':
    main()
