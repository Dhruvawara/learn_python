"""
To count no:of alphabets, numbers and special symbols using for loop
"""


def main():
    numbers = 0
    alphabets = 0
    special_symbols = 0
    string = input("Enter String : ")
    for element in string:
        if '0' <= element <= '9':
            numbers += 1
        elif 'a' <= element <= 'z' or 'A' <= element <= 'Z':
            alphabets += 1
        else:
            special_symbols += 1

    print(f"{numbers = }\n{alphabets = }\n{special_symbols = }")


if __name__ == '__main__':
    main()

# Sample Input : We are using python version 3.10.1
