# 4.  Write a Python program to check if a string is a palindrome.(IMP)
def using_loop(string):
    reverse = ''
    for char in string:
        reverse = char + reverse
    return f"{string} is a palindrome" if (reverse == string) else f"{string} is not a palindrome"

def single_line(string):
    return f"{string} is a palindrome" if string[::-1] == string else f"{string} is not a palindrome"

def using_join(string):
    return f"{string} is a palindrome" if ''.join(reversed(string)) == string else f"{string} is not a palindrome"

print(using_loop("mon"))
print(single_line("mon"))
print(using_join("mon"))