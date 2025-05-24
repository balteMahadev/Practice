# Write a program to count the occurrences of each word in a string and return MAX repeated words.(IMP)
def word_occurrences(string):
    words = string.lower().split()
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count


def max_occured_word(words):
    max_word = None
    max_count = 0
    for word, count in words.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word, max_count

def using_inbuilt_functions(string):
    words = string.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    max_word = max(word_counts, key=word_counts.get)
    return max_word, word_counts[max_word]


word = word_occurrences("this is a test this this only a test")
print(max_occured_word(word))
print(using_inbuilt_functions("this is a test this this only a test"))
