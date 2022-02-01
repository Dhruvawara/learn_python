"""
greatest of 4 numbers using nested conditions
"""
number_1 = int(input("Enter number 1:"))
number_2 = int(input("Enter number 2:"))
number_3 = int(input("Enter number 3:"))
number_4 = int(input("Enter number 4:"))
print(f"{number_1 = } {number_2 = } {number_3 = } {number_4 = }")
if number_2 <= number_1 >= number_3:
    if number_1 >= number_4:
        print(f"{number_1 = } is greater.")
elif number_4 <= number_2 >= number_3:
    print(f"{number_2 = } is greater.")
elif number_3 >= number_4:
    print(f"{number_3 = } is greater.")
else:
    print(f"{number_4 = } is greater.")

if number_1 > number_2:
    if number_1 > number_3:
        if number_1 > number_4:
            print(f"{number_1 = } is greater.")
        else:
            print(f"{number_4 = } is greater.")
    else:
        if number_3 > number_4:
            print(f"{number_3 = } is greater.")
        else:
            print(f"{number_4 = } is greater.")
else:
    if number_2 > number_3:
        if number_2 > number_4:
            print(f"{number_2 = } is greater.")
        else:
            print(f"{number_4 = } is greater.")
    else:
        if number_3 > number_4:
            print(f"{number_3 = } is greater.")
        else:
            print(f"{number_4 = } is greater.")

number_collection = [number_1, number_2, number_3, number_4]
number_collection.sort()
print(f"{number_collection[-1] = } is greater.")
