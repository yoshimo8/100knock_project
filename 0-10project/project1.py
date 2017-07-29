def devide(word):
    re_word = ''
    for i in  range(1, 8, 2):
        re_word += word[i]

    return(re_word)


print(devide('パタトクカシーー'))
