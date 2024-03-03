from random import randint
import copy


def check_input_matrix():
    while True:
        person_input_n = input("Введите кол-во столбцов: ")
        person_input_m = input("Введите кол-во строк: ")

        if person_input_m.isdigit() and person_input_n.isdigit():
            return int(person_input_n), int(person_input_m)
        else:
            print("Ошибка, повторите вход ")


def create_matrix(n, m):
    result = list()
    for _ in range(m):
        string = [randint(1, 9) for _ in range(n)]
        result.append(string)

    return result


# print(create_matrix(*check_input_matrix()))
