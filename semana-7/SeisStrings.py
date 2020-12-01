def main():

    str_model = input()
    diff = int(input())

    min_diff = diff * 2
    idx_min_diff = -1

    for i in range(5):
        str_sentence = input()
        diff_actual = 0

        for t in range(len(str_model)):
            if str_sentence[t] != str_model[t]:
                diff_actual += 1

        if diff_actual <= diff and diff_actual < min_diff:
            min_diff = diff_actual
            idx_min_diff = i + 1

    print('-1') if idx_min_diff == -1 else print(f'{idx_min_diff}\n{min_diff}')


main()
