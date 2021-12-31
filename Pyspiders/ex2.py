# given number is integer or not
num = input("Integer:")
try:
    if type(int(num)) == int:
        print(num, "is a integer")
except:
    print(num,"is not a integer")
