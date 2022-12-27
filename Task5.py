# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r") as my_f_1, \
        open(name_2, "r") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second):
            with open("poly_sum.txt", "a") as my_f_3:
                for i, v in enumerate(first):
                    my_f_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print("Содержимое файлов не совпадает!")


poly_sum("poly_1.txt", "poly_2.txt")