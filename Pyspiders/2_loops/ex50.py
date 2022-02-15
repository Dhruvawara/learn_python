"""
to check weather the given number is an perfect number or not
"""


def main():
    number = int(input("number = "))
    result = 0
    for num in range(1, number):
        if number % num == 0:
            result += num

    if result == number:
        print('Perfect Number')
    else:
        print("Not a Perfect Number")


if __name__ == '__main__':
    main()
