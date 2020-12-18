def main():
    data = {}
    n_people = int(input())

    for i in range(n_people):
        info = input().split(' ')
        data[info[0]] = info[1:]

    query = input()
    while query[0] != 'F':
        query = query.split(' ')
        print(
            'Uhul! Seu amigo secreto vai adorar' if query[1] in data[query[0]] else 'Tente Novamente!')

        query = input()


main()
