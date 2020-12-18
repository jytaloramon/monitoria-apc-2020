def main():
    [num1, num2] = map(int, input().split(' '))
    diff = bin(num1 - num2)
    len_str = len(diff)

    print(2 ** (len_str - 3), end='')
    for i in range(3, len_str):
        if(diff[i] != '0'):
            print(f' {(2 ** (len_str - i - 1))}', end='')

    print()


main()
