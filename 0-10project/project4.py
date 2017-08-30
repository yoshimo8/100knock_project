def word_sort(words):
    word_legend = {}
    numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    word_list = words.split()

    for word,i in zip(word_list,range(len(word_list))):
        if i in numbers:
            word_legend[word[1]] = i
        else:
            word_legend[word[0:2]] = i

    return(word_legend)

words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print(word_sort(words))
