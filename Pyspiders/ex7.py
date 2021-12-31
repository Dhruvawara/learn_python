# check character is uppercase or lowercase


character = input("Enter a character:")
if int(ord(character)) >= 65 and int(ord(character)) < 91:
    print(character, "is uppercase")
if int(ord(character)) > 96 and int(ord(character)) < 123:
    print(character, "is lowercase")
