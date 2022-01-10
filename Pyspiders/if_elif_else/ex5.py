# to find the greater number amon six numbers with the help of elif statement


def main():
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    c = int(input("enter the number"))
    d = int(input("enter the number"))
    e = int(input("enter the number"))
    f = int(input("enter the number"))
    if a > b and a > c and a > d and a > e and a > f:
        print(a, "is greater")
    elif b > c and b > d and b > e and b > f:
        print(b, " is greter")
    elif c > d and c > e and c > f:
        print(c, " is greter")
    elif d > e and d > f:
        print(d, " is greater")
    elif e > f:
        print(e, " is greater")
    else:
        print(f, " is greater")


if __name__ == "__main__":
    main()
