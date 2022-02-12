"""
wap to check wheather the given numbers is even or odd, if it is an even divide
the number by 2, if it is odd multiply number by 2 and store the result in separately
"""


def main():
    number_list = list(map(int, input("Enter number : ").strip().split()))
    result_list = []
    for value in number_list:
        if value % 2 == 0:
            result_list.append(value // 2)
        else:
            result_list.append(value * 2)

    print(f'{result_list = }')


def new_func():
    number_list = [25, 30, 65, 40, 75, 38, 75, 38, 22, 12, 11, 7, 6]
    result_list = []
    for value in number_list:
        if value % 2 == 0:
            result_list += [(value // 2)]
        else:
            result_list += [(value * 2)]

    print(f'{number_list = }\n{result_list = }')


if __name__ == '__main__':
    main()
    new_func()

# Sample input : 25 30 65 40 75 38 75 38 22 12 11 7 6
