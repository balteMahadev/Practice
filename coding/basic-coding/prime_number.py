# 8. Check if a number is prime.(IMP)
def prime_number(number):
    if number <= 1:
        return f"{number} is prime"
    for i in range(2, (number+1)//2):
        print(i)
        if number % i == 0:
            return f"{number} is not prime"
    return f"{number} is prime"

print(prime_number(13))
