# entered character is present in the string or not
string=input("Enter a String:")
character=input("Enter a Character:")
if character in string:
    print(character,'character is present in string',string)
if character not in string:
    print(character,'character is not present in string',string)