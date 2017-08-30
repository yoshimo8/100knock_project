#
# # 最初に書いたコード
# def sort_word(word):
#     legend_word = ''
#     word_list = word.split()
#     for i in range(0, 10):
#         for word in word_list:
#             try:
#                 legend_word += word[i]
#                 # legend_word.append(word[i])
#             except IndexError:
#                 pass
#
#     return legend_word
#
# words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#
# print(sort_word(words))

def sort_word(words):
    number_words_list = []
    word_list = words.split()
    for word in word_list:
        number_words_list.append(len(word))

    return number_words_list

words = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print(sort_word(words))
