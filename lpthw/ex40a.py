mystuff1 = {"apple": "I AM APPLES!"}
# Dictionary style
print(mystuff1["apple"])  # gets apple from dictionary

import mystuff

# Module style
mystuff.apple()  # gets apple from the module
print(mystuff.tangerine)  # same as above it's a variable


class MyStuffClass(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLE!")


# Class style
thing = MyStuffClass()
thing.apple()
print(thing.tangerine)
