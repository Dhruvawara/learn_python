"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def main():
    print(f"""
    {diffrent_numbers([2,4563,45,456,312,456,876,123,786,123,786,645,]) = }
    {diffrent_numbers([456,45645,6786,435213,4868,45678,64354516,4863483,456384,44645,]) = }
    {diffrent_numbers([8796,456,56,546,54,6,786,86,546,44,31,56,486,4,44,378,]) = }
    {diffrent_numbers([]) = }
    """)


def diffrent_numbers(input_data):
    
    removed_list = set()
    for value in input_data:
        if value in removed_list and ((value ** 2) % 2) != 0:
            return True, value
        removed_list.add(value)
    return False

if __name__ == '__main__':
    main()
()
