# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# from random import choice


# def polynomial(num: int):
    
#     poly = ""
#     num_list = range(0, 100)

#     with open("poly.txt", "a") as my_file:
#         for i in range(num, 0, -1):
#             value = choice(num_list)
#             if value:
#                 poly += f"{value}*x^{i} {choice('+-')} "

#         my_file.write(f"{poly}{choice(num_list)} = 0\n")


# for _ in range(3):
#     polynomial(int(input("Укажите степень многочлена: ")))

import random


def write_file(st):
    with open('file_k.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 100)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Задайте натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))