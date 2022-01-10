# to check whether the given input is single value data type or not. If it is True print SINGLE VALUE DATA TYPE then print the input value. Else just print MULTI VALUE DATA TYPE then print input value


def main():

    given_input = 123
    if type(given_input) in [int, float, complex, bool]:
        print(f"SINGLE VALUE DATA TYPE, {given_input = }")
    else:
        print(f"MULTI VALUE DATA TYPE, {given_input = }")


if __name__ == "__main__":
    main()
