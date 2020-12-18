def main():
    [limit, end_v] = map(int, input().split(' '))
    arr = []

    for i in range(limit):
        v = int(input())
        if v % 10 == end_v:
            arr.append(v)

    for i in range(5 - len(arr)):
        print('-1')

    arr.sort()
    for i in range(0 if len(arr) <= 5 else len(arr) - 5, len(arr)):
        print(arr[i])


main()
