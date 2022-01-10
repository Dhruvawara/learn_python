# to check weather the length of the list collection is even or odd, if it is even print the list collection else print middle value the list collection
def main():
    list_collection_input = input("Enter some string:")
    list_collection = list(list_collection_input)
    if len(list_collection_input) % 2 == 0:
        print(f"{list_collection = }")
    else:
        print(f"{list_collection[len(list_collection) // 2] = }")


if __name__ == "__main__":
    main()
