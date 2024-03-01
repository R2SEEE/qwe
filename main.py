import sys


def fun_val(n, k):
    """
    функция определяет число Вудала и
    определяеться ли оно кратным 3-ем
    """
    if (n + 2) > k:
        x = n * k**n - 1
        if x % 3 == 0:
            print("полученное число является кратным трём.")
        print("полученное число не является кратным трём.")

    else:
        print("данное число не являеться числом Вудала")


def check():
    n_num, k_num = input(), input()
    if n_num.isinstance() and k_num.isinstance():
        while True:
            fun_val(n_num, k_num)
            print("Хотите выйти yes or not")
            person = input()
            if person == "yes":
                sys.exit(1)
            else:
                print("Повторите ввод")


if "__main__" == __name__:
    pass
