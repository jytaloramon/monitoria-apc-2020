def main():
    value = int(input())

    for i in range(1, value // 2 + 1, (1 if value % 2 == 0 else 2)):
        if value % i == 0:
            print(i)
    print(value)


main()
