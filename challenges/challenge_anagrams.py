def insertion_sort(words):
    word = list(words.lower())
    n = len(word)
    for index in range(1, n):
        key = word[index]

        new_position = index - 1
        while new_position >= 0 and word[new_position] > key:
            word[new_position + 1] = word[new_position]
            new_position = new_position - 1
            word[new_position + 1] = key

    return "".join(word)


def is_anagram(first_string, second_string):
    word_1 = insertion_sort(first_string.lower()) 
    word_2 = insertion_sort(second_string.lower())

    if word_1 == "" or word_2 == "":
        return (word_1, word_2, False)
    elif word_1 != word_2:
        return (word_1, word_2, False)
    elif word_1 == word_2:
        return (word_1, word_2, True)
