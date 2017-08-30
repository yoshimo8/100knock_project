def ngram(words):
    word_list = words.split()
    unigram = word_list
    bigram = []

    for i in range(-1,len(word_list), 1):
        try:
            make_bigram = word_list[i] + '-' + word_list[i+1]
            bigram.append(make_bigram)
        except:
            pass

    return(unigram, bigram)

words = "I am an NLPer"
print(ngram(words))
