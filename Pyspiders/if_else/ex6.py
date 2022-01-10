# to check whether given char is vowel or not. If it vowel print 'VOWEL' then print ASCII value of the char along with the char. Else print ASCII value along with the char.


def main():
    input_character = input("Enter character: ")
    if input_character in "aeiouAEIOU":
        print(f"VOWEL, {ord(input_character) = }, {input_character = }")
    else:
        print(f"{ord(input_character) = }, {input_character = }")


if __name__ == "__main__":
    main()
