"""
to convert string into list of words at end of word add length of word
"""


def main():
    string = input("->")
    temp = ''
    list_var = []
    for char in string:
        if char == ' ':
            if temp:
                list_var += [temp + str(len(temp))]
                temp = ''
        else:
            temp += char
    if temp:
        list_var += [temp + str(len(temp))]
    print(f"{list_var = }")

    temp = ''
    list_var = []
    index = 0
    while index <= (len(string) - 1):
        if string[index] == ' ':
            if temp:
                list_var += [temp + str(len(temp))]
                temp = ''
        else:
            temp += string[index]
        index += 1
    if temp:
        list_var += [temp + str(len(temp))]
    print(f"{list_var = }")


if __name__ == '__main__':
    main()
