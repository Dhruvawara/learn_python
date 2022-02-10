"""
string in form of list reversed
"""


def main():
    string = input("->")
    temp = ''
    list_var = []
    for char in string:
        if char == ' ':
            if temp:
                list_var += [temp[::-1]]
                temp = ''
        else:
            temp += char
    if temp:
        list_var += [temp[::-1]]
    print(f"{list_var = }")

    temp = ''
    list_var = []
    index = 0
    while index <= (len(string) - 1):
        if string[index] == ' ':
            if temp:
                list_var += [temp[::-1]]
                temp = ''
        else:
            temp += string[index]
        index += 1
    if temp:
        list_var += [temp[::-1]]
    print(f"{list_var = }")


if __name__ == '__main__':
    main()
