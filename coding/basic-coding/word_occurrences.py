# 7. Write a program to count the occurrences of each word in a string.(IMP)
def word_occurrences(sentance):
    words = sentance.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def word_occurrences_optimese(sen):
    words = sen.lower().split()
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return words_count

print(word_occurrences("hi hi hi hello hello hi bye"))
print(word_occurrences_optimese("hi hi hi hello hello hi bye"))