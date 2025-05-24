# 1. How do you swap two variables without using a third variable?
def swiping_of_two_numbers_without_temp(number1, number2):
    number1, number2 = number2, number1
    return number1, number2

# 2. How do you swap two variables with using Arithmetic Operations?
def swiping_of_two_numbers_with_arithmetic_operations(number1, number2):
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    return number1, number2

# 2. How do you swap two variables with using temp?
def swiping_of_two_numbers_with_temp(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    return number1, number2

number1, number2 = swiping_of_two_numbers_with_temp(1, 2)
print(number1, number2)
number_1, number_2 = swiping_of_two_numbers_with_arithmetic_operations(10, 20)
print(number_1, number_2)
num1, num2 = swiping_of_two_numbers_with_temp(100, 200)
print(num1, num2)

