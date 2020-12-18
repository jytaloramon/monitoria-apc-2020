def main():
    n_books = int(input())
    n_students = int(input())

    proportion = n_students // n_books

    if proportion <= 8:
        print('A')
    elif proportion <= 12:
        print('B')
    elif proportion <= 18:
        print('C')
    else:
        print('D')

main()
