"""
Convert to lower case of given string using for loop
"""


def main():
    print(f'{to_lower_case("Dhruva") = }\n{to_lower_case("PYTHON") = }')


def to_lower_case(string):
    result = ''
    for character in range(len(string)):
        if 'A' <= string[character] <= 'Z':
            result = result + chr(ord(string[character]) + 32)
        else:
            result += string[character]
    return result


if __name__ == '__main__':
    main()
