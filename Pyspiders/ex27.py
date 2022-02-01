"""
to reverse an string using for loop
"""


def main():
    r_string = ''
    string = input('String : ')
    # Using indexing
    for index in range(-1, -len(string)-1, -1):
        r_string = r_string + string[index]
    print(f'{r_string = }')
    # Using Concatenation
    r_string = ''
    for value in string:
        r_string = value + r_string
    print(f'{r_string = }')


if __name__ == '__main__':
    main()
