# character present in the collection or not
string = input("String:")
character = input("Character:")
if character in string:
    print(character, "present in", string)
else:
    print(character, "not present in", string)
