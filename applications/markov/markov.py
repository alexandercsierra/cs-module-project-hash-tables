import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
def make_words_table(text):
    words_list = text.split()
    cache = {}

    # for i in range(len(words_list)-1):
    #     if words_list[i] in cache:
    #         cache[words_list[i]] += f" {words_list[i+1]}"
    #     else:
    #         cache[words_list[i]] = words_list[i+1]  
    # return cache  

    for i in range(len(words_list)-1):
        if words_list[i] in cache:
            cache[words_list[i]].append(words_list[i+1])
        else:
            cache[words_list[i]] = [words_list[i+1]]
    return cache  


sentence = "Cats and dogs and birds and fish dogs birds"
print(make_words_table(sentence))


# TODO: construct 5 random sentences
# Your code here
def make_random_sentences(text):
    cache = make_words_table(text)
    random_word = random.choice(text.split())

    stop_conditions = ['.', '?', '!', '."', '?"', '!"']

    curr = cache[random_word]
    sentence = random_word

    while curr[-1] not in stop_conditions or curr[-2:] not in stop_conditions:
        sentence = sentence + " " + curr



