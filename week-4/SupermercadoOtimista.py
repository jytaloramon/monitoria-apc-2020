def main():
    days = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

    day = int(input('Digite dia da semana: (1-SEG a 7-DOM)\n'))
    price_product = float(input('Digite preco do produto em reais:\n'))
    opt_product = int(input('Digite a opcao do produto: (2-prata 1-ouro)\n'))

    if day < 4 and opt_product == 1:
        price_product /= 2
    elif day >= 4 and day < 6 and 10 < price_product < 100:
        price_product /= 3
    elif day == 6 and opt_product == 2:
        price_product *= 3
    else:
        price_product *= 2

    print(f'O preco do produto no dia {days[day - 1]} e R$ {price_product:.2f}')


main()
