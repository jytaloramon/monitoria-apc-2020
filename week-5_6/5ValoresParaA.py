def main():
    count_negative = 0

    for i in range(5):
        value = input('Digite um valor:\n')
        if value[0] == '-':
            count_negative += 1

    print(f'Foram digitados {count_negative} numeros negativos')


main()
