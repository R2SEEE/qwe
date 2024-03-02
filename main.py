import sys


def fun_val(n, k):
    """
    функция определяет число Вудала и
    определяеться ли оно кратным 3-ем
    """
    if (n + 2) > k:
        x = n * k ** n - 1
        if x % 3 == 0:
            print("полученное число является кратным трём.")
        else:
            print("полученное число не является кратным трём.")

    else:
        print("данное число не являеться числом Вудала")


def check():
    while True:
        n_num, k_num = input('Введи число n: '), input('Введи число k: ')
        try:
            fun_val(float(n_num), float(k_num))
            person = input("Хотите выйти yes or not: ")
            if person == "yes":
                sys.exit(1)
            else:
                print("Повторите ввод")
        except:
            print("Ошибка входных данных, повторите ввод")


if "__main__" == __name__:
    check()
