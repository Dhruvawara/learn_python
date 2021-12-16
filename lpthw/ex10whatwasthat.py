tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# 1 -> Use single-qout instead of double qouts
fat_cat_single_qout = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fat_cat_single_qout)

# Escape character \ to print non characters like \ " '
# Escape        What It does
# \\            Backslash(\)
# \'            Single-quote(')
# \"            Double-qoute(")
# \a            ASCII bel (BEL)
# \b            ASCII backspace (BS)
# \f            ASCII formfeed (FF)
# \n            ASCII linefeed (LF)
# \N{name}      Character named name in the Unicode database(Unicode only)
# \r            Carriage return(CR)
# \t            Horizontal tab(TAB)
# \uxxxx        Character with 16-bit hex value xxxx
# \Uxxxxxxxx    Character with 32-bit hex value xxxxxxxx
# \v            ASCII vertical tab(VT)
# \000          Character with octal value 000
# \xhh          Character with hex value hh

print(
    """
\\  -> \
newline continued
\\\\    -> a \\ b
\\'     -> a \' b
\\"     -> a \" b
\\a     -> a \a b
\\b     -> a \b b
\\f     -> a \f b
\\n     -> a \n b
\\N{Multiplication sign}    -> a \N{Multiplication sign} b
ab\\r -> a \r b
\\t     -> a \t b
\\u007E -> a \u007E b
\\U0000007E -> a \U0000007E b
\\v     -> a \v b
\\176   -> a \176 b
\\x7E   -> a \x7E b
"""
)