import re

def word_count(text):
    word_count = {}
    word_list = text.split()
    for word in word_list:
        word = re.sub(r'[^\w\']', '', word)
        word = word.lower()
        if word in word_count:
            word_count[word] += "#"
        else:
            if word != '':
                word_count[word] = "#"
    items = list(word_count.items())
    items.sort(key=lambda e: len(e[1]))
    word_count = dict(items)
    for word in word_count:
        print(f'{word} {word_count[word]}\n')



word_count('hello hello ha ha ha hello ha')
