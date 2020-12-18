def main():

    account = float(input())
    n_func = int(input())
    max_pag = {'name': '', 'value': 0.0}
    sum_t = 0.0

    for i in range(n_func):
        name, value = input(), float(input())
        sum_t += value

        if value > max_pag['value']:
            max_pag['name'] = name
            max_pag['value'] = value

    if sum_t >= account:
        print(
            f'{max_pag["name"]} pagou R$ {max_pag["value"]}\nValor excedente: sobra R$  {(sum_t - account)}')
    else:
        if sum_t != 0:
            print(
                f'{max_pag["name"]} pagou R$ {max_pag["value"]}\nValor insuficiente: falta R$  {(account - sum_t)}')
        else:
            print('Nao ha conta ou funcionario suficiente para pagar a conta')


main()
