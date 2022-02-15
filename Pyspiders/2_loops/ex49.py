"""
to check weather the given number is an Armstrong or not with n digits
"""


def main():
    number = int(input("Number = "))
    result = 0
    temp = number
    digits = len(str(number))
    while number > 0:
        print(f"Initail\t{result = }\t{number = }")
        remainder = number % 10
        result += remainder ** digits
        number = number // 10
        print(f"End\t{remainder = }\t{result = }\t{number = }\n")

    if result == temp:

        print("Armstrong number")
    else:
        print("Not Armstrong number")


if __name__ == '__main__':
    main()
