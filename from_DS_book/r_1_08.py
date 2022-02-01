"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤k < 0, what is the equivalent index j ≥0 such that s[j] references
the same element?
"""


def main():
    print(f'''
    {negative_to_positive_index("Dhruva", -3) = }
    {negative_to_positive_index("Hello, World!",-11) = }
    ''')


def negative_to_positive_index(string, index):
    p_index = len(string) + index
    return string[index], p_index, string[p_index]


if __name__ == '__main__':
    main()
