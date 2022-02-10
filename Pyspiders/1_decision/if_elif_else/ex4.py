# to find the greater number among three numbers by using elif statement


def main():
    # greatest of 4 numbers
    num1 = int(input("A:"))
    num2 = int(input("B:"))
    num3 = int(input("C:"))
    if num2 <= num1 >= num3:
        print(num1, "is greatest")
    elif num1 <= num2 >= num3:
        print(num2, "is greatest")
    else:
        print(num3, "is greatest")


if __name__ == "__main__":
    main()
