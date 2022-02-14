"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""


def main():
    string = input("String : ")
    print(punctuation_remove(string))


def punctuation_remove(s):
    output_string = ''
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ':
            output_string += char
    return output_string


if __name__ == '__main__':
    main()
