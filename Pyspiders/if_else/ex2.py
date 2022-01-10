# to check weather the given alphabet is lower case alphabet or not, if it is true print LOWER then print that alphabet, else print UPPER then print that alphabet.


def main():
    character = input("Enter a character: ")
    if "a" <= character <= "z":
        print("LOWERCASE:", character)
    else:
        print("UPPERCASE:", character)


if __name__ == "__main__":
    main()
