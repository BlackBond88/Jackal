def counter(n):
    """ Вычисляет следующий элемент последовательности """
    x1 = 0
    x2 = 1
    for i in range(n):
        x2 += x1
        print(i, '-й элемент: ', x1, sep='')
        x1 = x2 - x1


def main():
    try:
        n = int(input('Введите количество элементов последовательности Фибоначчи: '))
        if n <= 0:
            raise Exception
        counter(n)
    except Exception:
        print('Ошибка ввода!')
        main()


if __name__ == '__main__':
    main()
