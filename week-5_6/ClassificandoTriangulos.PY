def main():

    values = input()
    while values[0] != 'F':
        [a, b, c] = list(map(int, values.split(' ')))

        if not (a < b + c) or not (b < a + c) or not (c < a + b):
            print('INVALIDO')
        elif a == b and b == c:
            print('EQUILATERO')
        elif a != b and a != c and b != c:
            print('ESCALENO')
        else:
            print('ISOSCELES')

        values = input()


main()
