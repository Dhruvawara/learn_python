"""
to check weather the given number is prime or not between range
"""


def main():
    start_number = int(input("Start number -> "))
    end_number = int(input("End number -> "))

    for number in range(start_number, end_number+1):
        for num in range(2, (number // 2 + 1)):
            if number % num == 0:
                print('Number {} is not prime'.format(number))
                break
        else:
            print('Number {} is prime'.format(number))

    print()
    while start_number <= end_number:
        number = start_number
        num = 2
        while num <= (number // 2):
            if number % num == 0:
                print('Number {} is not prime'.format(number))
                break
            num += 1
        else:
            print('Number {} is prime'.format(number))
        start_number += 1


if __name__ == '__main__':
    main()
