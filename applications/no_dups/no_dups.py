def no_dups(s):
    cache = {}
    word_list = s.split()
    new_str_list = []

    for word in word_list:
        if word not in cache:
            cache[word] = 1
            new_str_list.append(word)
    return " ".join(new_str_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))