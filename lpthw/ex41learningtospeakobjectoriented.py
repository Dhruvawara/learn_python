# import random module
import random
#  import urllib.request feature from urlopen module
from urllib.request import urlopen
# import sys module
import sys

# link to list of words
WORD_URL = "http://learncodethehardway.org/words.txt"
# WORDS variable initialized as list
WORDS = []

# Dictionary variable PHRASES
PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)": "class %%% has-a __init__ that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'.",
}

# For English to code
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
# for code to english
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # append to WORDS list after striping the space from beginning and end
    WORDS.append(str(word.strip(), encoding="utf-8"))

# used to convert patterned words and with words taken from internet[p']
def convert(snippet, phrase):
    # because class names start with capital so to differentate,using capitalize method
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # other names for other patterns
    other_names = random.sample(WORDS, snippet.count("***"))
    # for names
    results = []
    # for parameters
    param_names = []

    # for parameters
    for i in range(0, snippet.count("@@@")):
        # parameters can range from 1 to 3
        param_count = random.randint(1, 3)
        # append 1 to 3 words
        param_names.append(" ".join(random.sample(WORDS, param_count)))

    # replacing the pattern with words
    for sentence in snippet, phrase:
        # putting the key and value of the dict to result listvariable
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***",word,1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit control-D
try:
    while True:
        # getting key values
        snippets = list(PHRASES.keys())
        # shuffling the keys
        random.shuffle(snippets)

        # going through all the items in the dict
        for snippet in snippets:
            # getting value
            phrase = PHRASES[snippet]
            # putting words into the patterns
            question, answer = convert(snippet, phrase)
            # to change if it's question to code
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
