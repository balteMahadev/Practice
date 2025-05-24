# 1. Write a program to check if a number is even or odd.
def even_odd(number):
    if number % 2 == 0:
        return f"{number} is EVEN"
    else:
        return f"{number} is ODD"

def single_line(number):
    return f"{number} is EVEN" if number % 2 == 0 else f"{number} is ODD"

print(even_odd(10))
print(single_line(11))