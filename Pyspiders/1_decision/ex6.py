# check weather given character is number or not
num = input("Enter single character:")
if int(ord(num)) >= 48 and int(ord(num)) < 58:
    print(num, "is a number.")
if not (int(ord(num)) >= 48 and int(ord(num)) < 58):
    print(num, "is not a number.")
