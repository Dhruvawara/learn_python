"""
to count no of words present in a string
"""


def main():
    string = input("->")
    temp = ''
    count = 0
    for char in string:
        if char == ' ':
            count += 1
            temp = ''
        else:
            temp += char
    if temp:
        count += 1
    print(f"{count = }")


if __name__ == '__main__':
    main()
