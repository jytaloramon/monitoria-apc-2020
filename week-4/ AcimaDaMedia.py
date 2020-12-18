def main():
    grades = [float(input()), float(input()), float(input())]
    avg = sum(grades) / 3
    count = 0

    for i in range(3):
        if grades[i] > avg:
            count += 1

    print(count)


main()
