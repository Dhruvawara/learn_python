"""
Had we implemented the scale function (page 25) as follows, does it work
properly?
    def scale(data, factor):
        for val in data:
            val = factor 
Explain why or why not.
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
