"""
WAP to print even numbers and odd numbers seperately from the given list
if it is an even store in an even list,if it is odd store in odd list.
"""


def main():
    even_list = []
    odd_list = []
    numbers_list = list(
        map(int, input("Enter number in (n n n) : ").strip().split()))
    print(f'{numbers_list = }')

    for value in numbers_list:
        if value % 2 == 0:
            even_list.append(value)
        else:
            odd_list.append(value)

    print(f'{even_list = }\n{odd_list = }')


def new_func():
    number_list = [25, 30, 65, 40, 75, 38, 75, 38, 22, 12, 11, 7, 6]
    even_list = []
    odd_list = []

    print(f'{number_list = }')

    for value in number_list:
        if value % 2 == 0:
            even_list += {value}
        else:
            odd_list += [value]

    print(f'{even_list = }\n{odd_list = }')


if __name__ == '__main__':
    main()
    new_func()

# Sample input =  25 30 65 40 75 38 75 38 22 12 11 7 6
