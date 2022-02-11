"""
b = [5, 10, 15, 2.5, 'hai', 3+4j, 20, 50, 60.5]
sum of integers
"""


def main():
    b = [5, 10, 15, 2.5, 'hai', 3+4j, 20, 50, 60.5]
    sum = 0
    for value in b:
        if type(value) == int:
            sum += value
    print(f"{sum = }")

    sum = 0
    index = 0
    while index < len(b):
        if type(b[index]) == int:
            sum += b[index]
        index += 1
    print(f'{sum = }')


if __name__ == '__main__':
    main()
