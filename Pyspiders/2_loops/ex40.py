"""
to print series of factorial between the range
"""


def main():
    start = int(input("Start -> "))
    end = int(input("End -> "))

    for value in range(start, (end + 1)):
        factorial = 1
        if value == 0:
            factorial = 1
        for fact_value in range(1, (value + 1)):
            factorial *= fact_value
        print('factorial({}) : {}'.format(value, factorial))

    while start <= end:
        factorial = 1
        number = 1
        if start == 0:
            factorial = 1
        while number <= start:
            factorial *= number
            number += 1
        print('factorial({}) : {}'.format(start, factorial))
        start += 1


if __name__ == '__main__':
    main()
