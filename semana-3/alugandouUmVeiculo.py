def main():
    days = int(input())
    distance = int(input())

    over_distance = distance - (days * 100)

    total = (days * 90.0 if over_distance <=
             0 else days * 90.0 + over_distance * 12)

    print(f'{(total):.2f}')


main()
