def re(words):
    re_words = ''
    for i in reversed(words):
        re_words += i

    return re_words

print(re('stressed'))
