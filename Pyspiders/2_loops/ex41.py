"""
to check weather the given number is prime or not
"""


def main():
    number = int(input("number -> "))
    prime = True
    for num in range(2, (number // 2 + 1)):
        if number % num == 0:
            prime = False
    if prime:
        print('Number {} is prime'.format(number))
    else:
        print('Number {} is not prime'.format(number))

    prime = True
    num = 2
    while num <= (number // 2):
        if number % num == 0:
            prime = False
        num += 1
    if prime:
        print('Number {} is prime'.format(number))
    else:
        print('Number {} is not prime'.format(number))

    for num in range(2, (number // 2 + 1)):
        if number % num == 0:
            print('Number {} is not prime'.format(number))
            break
    else:
        print('Number {} is prime'.format(number))

    num = 2
    while num <= (number // 2):
        if number % num == 0:
            print('Number {} is not prime'.format(number))
            break
        num += 1
    else:
        print('Number {} is prime'.format(number))


if __name__ == '__main__':
    main()
