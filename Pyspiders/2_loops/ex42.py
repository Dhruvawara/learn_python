"""
length of string without using len()
"""


def main():
    string = input("-> ")
    count = 0
    for value in string:
        count += 1
    print(f"{count = }")

    count = 0
    initail = 0
    while initail < len(string):
        count += 1
        initail += 1
    print(f"{count = }")


if __name__ == '__main__':
    main()
