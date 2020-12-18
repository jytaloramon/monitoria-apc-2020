def main():
    """
    dist_run: distância a ser percorrida
    money_safe: dinheiro que não foi usado
    fuel: quantidade de combustível
    n_fuel_reload: quantidade de postos no percurso
    price_fuel_reload: preço do lítro de combustível
    """

    [dist_run, money_safe, fuel, n_fuel_reload,
        price_fuel_reload] = map(int, str(input()).split(' '))

    # Distância até o primeiro posto
    space_fuel_reload = dist_run // (n_fuel_reload + 1)
    # Distância que poderá ser percorrida com o combustível atual
    dist_safe = fuel * 10
    # Distância faltante
    dead_fuel = dist_run - dist_safe

    if(dead_fuel <= 0):
        # Se o combustível der para chegar ao destino
        print(f'Pode viajar.\nR$: {money_safe}')
    elif dist_safe >= space_fuel_reload and dead_fuel // 10 * price_fuel_reload <= money_safe:
        # Caso o combustível atual der para chega ao posto "e" tenha dinheiro para completar até o destino
        print(
            f'Pode viajar.\nR$: {money_safe - (dead_fuel // 10 * price_fuel_reload)}')
    else:
        # Caso não der para chegar
        print('Nao pode viajar.')


main()
