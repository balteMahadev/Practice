# Remove Duplicates from the String and arrange in a increasing order(IMP)
def remove_duplicates(string):
    chars = string.lower()
    unique_chars = []
    for char in chars:
        if char not in unique_chars and char != ' ':
            unique_chars.append(char)
    return unique_chars

def sorte_characters(str):
    for i in range(len(str)-1):
        for j in range(len(str)-i-1):
            if str[j] > str[j+1]:
                str[j], str[j+1] = str[j+1], str[j]
    return str

def combine_the_list(str):
    word = ''
    for char in str:
        word = word + char
    return word

def all_methods_in_one(str):
    chars = str.lower()
    unique_chars = []
    for char in chars:
        if char not in unique_chars and char != ' ':
            unique_chars.append(char)
    return ''.join(sorted(unique_chars))

print(combine_the_list(sorte_characters(remove_duplicates("hello"))))
print(all_methods_in_one("hello"))