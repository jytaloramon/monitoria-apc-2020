def main():

    value = int(input())
    while value != 0:
        # Último elemento da PA
        last_el = 1 + (value // 2 - 1) * 2
        # Soma da PA
        sum_t = (value // 2) * (1 + last_el) // 2
        print(value + sum_t, '-', sum_t)

        value = int(input())


main()
