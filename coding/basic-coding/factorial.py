# 5.  Write a function to find the factorial of a number.(IMP)
def factorial(number):
    fact = 1
    if number == 0 or number == 1:
        return fact
    else:
        for i in range(2, number+1):
            fact = fact * i
    return fact

def using_while_loop(number):
    fact = 1
    counter = 1
    while counter <= number:
        fact = fact * counter
        counter = counter + 1
    return fact

print(factorial(4))
print(using_while_loop(4))
