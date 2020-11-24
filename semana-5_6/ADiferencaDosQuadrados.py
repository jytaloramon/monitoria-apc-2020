def main():

    value = int(input())
    while value != 0:
        sum_t = sum(range(1, value, 2))
        print(value + sum_t, '-', sum_t)

        value = int(input())


main()
