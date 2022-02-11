"""
c = ['hai', 'mysore', 'hello', 'bangalore']
longest string
"""


def main():
    c = ['hai', 'mysore', 'hello', 'bangalore']
    longest = 0
    longest_index = None
    for index in range(len(c)):
        if len(c[index]) > longest:
            longest = len(c[index])
            longest_index = index
    print("Longest string is {} with length {}.".format(
        c[longest_index], longest))

    longest = 0
    longest_index = None
    index = 0
    while index < len(c):
        if len(c[index]) > longest:
            longest = len(c[index])
            longest_index = index
        index += 1
    print("Longest string is {} with length {}.".format(
        c[longest_index], longest))


if __name__ == '__main__':
    main()
