# Задать натуральное число N. Написать программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))
i = 2 
lst = []
dig = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'{dig} -> {lst}')