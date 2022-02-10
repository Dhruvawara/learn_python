"""
to check whether the given character is an alphabet or not if it is an alphabet then check the char is an vowel or consonant
"""


def main():
    character = input("Enter a character: ")
    if "a" <= character <= "z" or "A" <= character <= "Z":
        if character in "AEIOUaeiou":
            print(character, "is a vowel.")
        else:
            print(character, "is a consonant")


if __name__ == "__main__":
    main()
