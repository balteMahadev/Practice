# 10.  Find the sum of digits of a number.
def using_list(number):
    total = 0
    for digit in str(number):
        total = total + int(digit)
    return total

def using_while(number):
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

print(using_list(123456))
print(using_while(123456))
