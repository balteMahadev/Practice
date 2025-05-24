# 3.  Find the largest among three numbers?
def largest_of_3_numbers(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        return f"{num1} is largest number"
    elif num2 > num3:
        return f"{num2} is largest number"
    else:
        return f"{num3} is largest number"

def using_max(num1, num2, num3):
    return f"{max(num1, num2, num3)} is largest number"

def single_line(num1, num2, num3):
    return f"{num1} is largest number" if (num1 > num2 and num1 > num3) else (f"{num2} is largest number" if (num2 > num3) else f"{num3} is largest number")

print(largest_of_3_numbers(10, 20, 30))
print(using_max(10, 50, 30))
print(single_line(100, 20, 30))
