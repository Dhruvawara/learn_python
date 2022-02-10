# stored in same memory or not
a = [1, 2]
b = a
if b is a:
    print("Same memory address.")
b = a.copy()
if b is not a:
    print("Diffrent memory address.")
