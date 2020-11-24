def main():
    
    qt = int(input())
    sum_t = 0.0

    for i in range(qt):
        sum_t += float(input())

    print(round(sum_t / qt, 1))


main()
