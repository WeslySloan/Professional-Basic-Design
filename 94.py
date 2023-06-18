import string

char = "'!#$%&‚()*+,-./:;<=>?@[\]^_„{|}~"

text = ""
while True:
    try:
        line = input()
        if not line:
            break
        text += line + "\n"
    except EOFError:
        break

translator = str.maketrans("", "", char)
text = text.translate(translator)

text = text.lower()

print(text)
