"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] ·b[i], for i = 0, . . . , n −1.
"""


def main():
    length = int(input("Array length : "))
    a = list(map(int, input("a : ").split()))
    b = list(map(int, input("b : ").split()))
    c = [a[index] * b[index] for index in range(length)]
    print(f"{a = }\n{b = }\n{c = }")


if __name__ == '__main__':
    main()
