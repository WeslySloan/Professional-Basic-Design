import re

def extract_words(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = re.findall(r'\b\w+\b', cleaned_text)
    unique_words = list(set(words))
    sorted_words = sorted(unique_words)
    return sorted_words

text = []
while True:
    try:
        line = input()
        if line:
            text.append(line)
        else:
            break
    except EOFError:
        break

text = ' '.join(text)

words = extract_words(text)

for word in words:
    print(word)
