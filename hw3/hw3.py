# Вариант с тремя циклами
# print('Подсчет количества повторяющихся слов и поиск максимального')
# while 1:
#     print('Введите слова через пробел:')
#     words = input().lower().split()
#     popular_words = {}
#     for word in words:
#         if word in popular_words:
#             popular_words[word] += 1
#         else:
#             popular_words[word] = 1
#     max_pop = 1
#     for word in popular_words.values():
#         if word > max_pop:
#             max_pop = word
#     for word, pop in popular_words.items():
#         if pop == max_pop:
#             print(str(pop) + " - " + word)

# Вариант с двумя циклами
# print('Подсчет количества повторяющихся слов и поиск максимального')
# while 1:
#     print('Введите слова через пробел:')
#     word_list = input().lower().split()
#     word_set = set(word_list)
#     pop_words = dict()
#     max_count = 1
#     for word in word_set:
#         cur_count = word_list.count(word)
#         max_count = max(max_count, cur_count)
#         pop_words[word] = cur_count
#     for word, count in pop_words.items():
#         if count == max_count:
#             print(str(count) + " - " + word)

# Вариант с одним циклом
print('Подсчет количества повторяющихся слов и поиск максимального')
while 1:
    print('Введите слова через пробел:')
    word_list = input().lower().split()
    word_set = set(word_list)
    max_count = 1
    result = ""
    for word in word_set:
        cur_count = word_list.count(word)
        if max_count < cur_count:
            max_count = cur_count
            result = str(max_count) + " - " + word
        elif max_count == cur_count:
            result += "\n" + str(max_count) + " - " + word
    print(result)
