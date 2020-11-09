def main():
    values = sorted(map(int, input().split(' ')))
    sum_t = sum(values)
    
    # n1 + (n1 + 1) + (n1 + 2) + (n1 + 3) + (n1 + 4) = 5n + 10
    # n1 + (n1 + 1)² + (n1 + 2)² + (n1 + 3)² + (n1 + 4)² = 4n^2 + 21n + 30
    #
    # P = sqrt(min(values)):
    # P + (P + 1)² + (P + 2)² + (P + 3)² + (P + 4)²


    if (5 * values[0] + 10) == sum_t:
        print('Sim\nSomatoria I')
    elif (4 * values[0] ** 2 + 21 * values[0] + 30) == sum_t:
        print('Sim\nSomatoria II')
    else:
        multiple = round(values[0] ** (1 / 3), 2)
        i = 1
        while i < 5 and (multiple + i) ** 3 == values[i]:
            i += 1

        if i == 5:
            print('Sim\nSomatoria III')
        else:
            print('Nao pertence a nenhuma somatoria')


main()
