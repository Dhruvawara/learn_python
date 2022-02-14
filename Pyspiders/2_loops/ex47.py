"""
to check weather given number is an palindrome or not
"""


def main():
    number = int(input('Number : '))
    result = 0
    temp = number
    remainder = 0

    while number > 0:
        print(f"Initail\t{remainder = }\t{result = }\t{number = }")
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10
        print(f"End\t{remainder = }\t{result = }\t{number = }\n")

    if temp == result:
        print("PALLINDROME")
    else:
        print("NOT PALLINDROME")


if __name__ == '__main__':
    main()
