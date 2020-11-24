def main():
    start_n, end_n = int(input()), int(input())

    for x in range(start_n, end_n + 1):
        print((x ** 2 - 4 * x + 5))


main()
