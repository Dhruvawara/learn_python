"""
To count number of spaces present in an string
"""


def main():
    count = 0
    string = input("String : ")
    for value in string:
        if value == ' ':
            count += 1
    print(f"{count = }")


if __name__ == '__main__':
    main()
