"""
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor . We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""


def main():
    x = [1, 2, 3, 4, 5]
    print(f"""
    {scale(x, 1) = }
    {scale(x, 2) = }
    {scale(x, 3) = }
    {scale(x, 0) = }
    """)


def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    return data


if __name__ == '__main__':
    main()
