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
    cache[words_list[-1]] = []
    return cache  


sentence = "Cats and dogs and birds and fish dogs birds?"
# print(make_words_table(sentence))


# TODO: construct 5 random sentences
# Your code here
def make_random_sentences(text):
    cache = make_words_table(text)
    #random starting word from text
    random_word = random.choice(text.split())


    stop_conditions = ['.', '?', '!', '."', '?"', '!"']

    #set current to the array of words following the starting word
    current_words = cache[random_word]
    #set curr to be a random word in the value array
    curr = random.choice(current_words)
    #start sentence with the random word
    sentence = random_word
    # print('current', curr)
    # print('curr[-1]', curr[-1:])
    # print('curr[-2]', curr[-2:])
    while curr[-1] not in stop_conditions and curr[-2:]+ curr[-1] not in stop_conditions and len(cache[curr]) > 1:
        # print('curr', curr)
        # print('curr[-1]', curr[-1])
        if cache[curr] != [] and cache[curr] != None:
            # print('in the if', curr, cache[curr])
            sentence = sentence + " " + curr
            # print('cache[curr]', cache[curr])
            curr = random.choice(cache[curr])
            # print('curr after random', curr)
        else:
            curr = random.choice(current_words)            

    sentence += " " + curr
    print(sentence)

make_random_sentences(words)
make_random_sentences(words)
make_random_sentences(words)
make_random_sentences(words)
make_random_sentences(words)




