"""
to convert string into list of words
"""


def main():
    string = input("->")
    temp = ''
    list_var = []
    for char in string:
        if char == ' ':
            if temp:
                list_var += [temp]
                temp = ''
        else:
            temp += char
    if temp:
        list_var += [temp]
    print(f"{list_var = }")


if __name__ == '__main__':
    main()
