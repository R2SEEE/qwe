from random import randint


def create_matrix(n, m):
    result = list()
    for _ in range(m):
        string = [randint(1, 9) for _ in range(n)]
        result.append(string)

    return result


n = int(input("столбцы"))
m = int(input("строки"))
