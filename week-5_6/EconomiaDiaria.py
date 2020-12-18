def main():
    count = 0

    sum_t = last = float(input())
    for i in range(6):
        actual = float(input())

        if actual - last >= 0.5:
            count += 1

        last = actual
        sum_t += actual

    print(f'R$ {sum_t:.2f}\n{count}')


main()
