"""
check weather character is alphabet,number,special symbol
"""
character = input("Character:")
if "A" <= character <= "Z" or "a" <= character <= "z":
    print(character, "is a alphabet.")
elif "0" <= character <= "9":
    print(character, "is a number")
else:
    print(character, "is a special symbol")
