"""
greatest of 4 numbers
"""

num1 = int(input("A:"))
num2 = int(input("B:"))
num3 = int(input("C:"))
num4 = int(input("D:"))
if num2 <= num1 >= num3 and num1 >= num4:
    print(num1, "is greatest")
elif num1 <= num2 >= num3 and num2 >= num4:
    print(num2, "is greatest")
elif num1 <= num3 >= num4 and num3 >= num1:
    print(num3, "is greatest")
else:
    print(num4, "is greatest")
