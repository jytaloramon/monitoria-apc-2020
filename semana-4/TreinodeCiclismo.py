def main():

    count = 0
    msg = ''

    for i in range(7):
        dist = float(input())
        if dist >= 8:
            count += 1

    if count >= 5:
        msg = 'Desempenho otimo'
    elif count >= 3:
        msg = 'Desempenho razoavel'
    else:
        msg = 'Desempenho ruim'

    print(msg)


main()
