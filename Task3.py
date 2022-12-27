# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

def fill_number_list(n=10, min=1, max=9) -> list:
    number_list = [random.randint(min, max)]
    for i in range (1, n):
        number_list.append(random.randint(min, max)) 
    return number_list

def unique_values_list(user_list) -> list:
    new_list = [user_list[0]]
    for i in range(1, len(user_list)):
        for j in range(len(new_list)):
            if user_list[i] == new_list[j]:
                break
            elif j == len(new_list)-1:
                new_list.append(user_list[i])
    return new_list

source_list = fill_number_list(10, 1, 10)
unique_list = unique_values_list(source_list)
print(f'{source_list} -> {unique_list}')