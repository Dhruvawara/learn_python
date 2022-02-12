"""
Write a short Python function that counts the number of vowels in a given
character string.
"""


def main():
    vowels = 0
    string = input("String : ")
    for char in string:
        if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowels += 1
    print("Vowels = {}".format(vowels))


if __name__ == '__main__':
    main()
