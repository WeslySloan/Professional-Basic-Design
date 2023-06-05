import sys
import string

def punc_remove(text):
    #special_char = '!#$%&‚()*+,-./:;<=>?@[\]^_„{|}~'
    #string.punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")
    text = text.lower()
    return text

st = sys.stdin.readlines()

for i in st:
    print(punc_remove(i), end="")
