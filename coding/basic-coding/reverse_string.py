# 6.  Implement a program to reverse a string.(IMP)
def reverse_string(string):
    return string[::-1]

def reverse_using_loop(string):
    reverse = ''
    for char in string:
        reverse = char+reverse
    return reverse

def reverse_using_keyword(string):
    return ''.join(reversed(string))


print(reverse_string("hello"))
print(reverse_using_loop("hello"))
print(reverse_using_keyword("hello"))