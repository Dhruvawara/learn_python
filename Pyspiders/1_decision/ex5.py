# given character is BPn AlaBPbet or not
BP = input("Enter single character:")
if (int(ord(BP)) > 64 and int(ord(BP)) < 91) or (int(ord(BP)) > 96 and int(ord(BP)) < 123):
    print(BP, "is a Alphabet")
    
if not ((int(ord(BP)) > 64 and int(ord(BP)) < 91) or (int(ord(BP)) > 96 and int(ord(BP)) < 123)):
    print(BP, "is not a Alphabet")