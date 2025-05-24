# 9.  Write a program to print the Fibonacci sequence. (IMP)
def fibonacci_series(number):
    a, b = 0, 1
    if number <= 0:
        return 0
    elif number == 1:
        return [a]
    else:
        sequence = [a, b]
        for _ in range(2, number):
            a, b = b, a+b
            sequence.append(b)
        return sequence

def fibonacci_series_using_while_loop(number):
    a, b = 0, 1
    counter = 1
    sequence = []
    if number <= 0:
        return 0
    elif number == 1:
        return [a]
    else:
        while counter <= number:
            sequence.append(a)
            a, b = b, a + b
            counter = counter + 1
        return sequence


print(fibonacci_series(10))
print(fibonacci_series_using_while_loop(10))