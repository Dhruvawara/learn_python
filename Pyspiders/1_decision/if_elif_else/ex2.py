# to check whether the given integer number is having single digit or two digit or three digit or than these digits.
def main():
    integer = int(input("INTEGER: "))
    if len(str(integer)) == 1:
        print("SINGLE")
    elif len(str(integer)) == 2:
        print("DOUBLE")
    elif len(str(integer)) == 3:
        print("TRIPLE")
    else:
        print("MORE THAN 3")


if __name__ == "__main__":
    main()
