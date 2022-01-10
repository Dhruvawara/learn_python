# to predict the grade obtained by the student based on his result percentage.


def main():
    grade = int(input("GRADE: "))
    if 90 <= grade <= 100:
        print("A")
    elif grade > 60:
        print("B")
    else:
        print("C")


if __name__ == "__main__":
    main()
