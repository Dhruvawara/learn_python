"""
in form of dictionary string : len of string
"""


def main():
    string = input("->")
    temp = ''
    dict_var = {}
    for char in string:
        if char == ' ':
            if temp:
                dict_var[temp] = len(temp)
                temp = ''
        else:
            temp += char
    if temp:
        dict_var[temp] = len(temp)
    print(f"{dict_var = }")
    
    temp = ''
    dict_var = {}
    index = 0
    while index <= (len(string) - 1):
        if string[index] == ' ':
            if temp:
                dict_var[temp] = len(temp)
                temp = ''
        else:
            temp += string[index]
        index += 1
    if temp:
        dict_var[temp] = len(temp)
    print(f"{dict_var = }")


if __name__ == '__main__':
    main()
