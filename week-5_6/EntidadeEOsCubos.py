def main():
    """
    Nível 1: 1 cubo
    Nível 2: 1 + 2 = 3 cubos
    Nível 3: 1 + 2 + 3 = 6 cubos

    Generalização: n = nível;
    Soma do Nível = 1 + ... + (n - 2) + (n - 1) + n 
        => n ** 2 - [(n - 1) * n / 2]
    """

    cube = int(input())

    if cube < 2:
        print(cube)
    else:
        level = 2
        sum_used = 1

        qt_level = level ** 2 - ((level - 1) * level // 2)
        while sum_used + qt_level <= cube:
            sum_used += qt_level
            level += 1
            qt_level = level ** 2 - ((level - 1) * level // 2)

        print(level - 1)


main()
