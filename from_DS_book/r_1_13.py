"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""


def main():
    input_data = [n for n in range(10)]
    print(f"{input_data = }")

    reversed_data = []
    for value in input_data:
        reversed_data = [value] + reversed_data
    print(f"{reversed_data = }")

    print(f"{list(reversed(input_data)) = }")

    print(f"{input_data = }")
    input_data.reverse()
    print(f"input_data.reverse() = {input_data}")


if __name__ == '__main__':
    main()
