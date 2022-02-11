"""
a='python is easy'
output : nohtyp si ysae
"""


def main():
    a = 'python is easy'
    reverse_a = ''
    temp = ''
    for char in a:
        if char == ' ':
            if temp:
                reverse_a += temp + ' '
                temp = ''
        else:
            temp = char + temp
    if temp:
        reverse_a += temp
    print(f'{reverse_a = }')

    reverse_a = ''
    temp = ''
    index = 0
    while index < len(a):
        if a[index] == ' ':
            if temp:
                reverse_a += temp + ' '
                temp = ''
        else:
            temp = a[index] + temp
        index += 1
    if temp:
        reverse_a += temp
    print(f'{reverse_a = }')


if __name__ == '__main__':
    main()
