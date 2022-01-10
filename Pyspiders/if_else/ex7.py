# to check whether the given input is tuple or not. If it is a tuple and length of that tuple is even print that tuple collection with length else print INVALID


def main():
    input_tuple = (1, 2, 3)
    if type(input_tuple) == tuple and len(input_tuple) % 2 == 0:
        print(f"{input_tuple = } {len(input_tuple) = }")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
