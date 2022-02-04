"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""


def main():
    print(f"""
    {diffrent_numbers([2,4563,45,456,312,456,876,123,786,123,786,645,]) = }
    {diffrent_numbers([456,45645,6786,435213,4868,45678,64354516,4863483,456384,44645,]) = }
    {diffrent_numbers([8796,456,56,546,54,6,786,86,546,45,31,56,486,4,45,378,]) = }
    {diffrent_numbers([]) = }
    """)


def diffrent_numbers(input_data):
    removed_list = set()
    for value in input_data:
        if value in removed_list:
            return True, value
        removed_list.add(value)
    return False


if __name__ == '__main__':
    main()
