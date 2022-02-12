"""
wap to print all the even numbers between the input range
"""


def main():
    start_number = int(input("Enter Start number : "))
    end_number = int(input("Enter end number : "))
    print('Even numbers : ', end=' ')
    for value in range(start_number, end_number + 1):
        if value % 2 == 0:
            print(value, end=' ')


if __name__ == '__main__':
    main()
