def main():

    number_comp, point_min = int(input()), int(input())
    count_comp_hab = 0

    for i in range(number_comp):
        level_1, lavel_2 = int(input()), int(input())

        if level_1 != 0 and lavel_2 != 0 and level_1 + lavel_2 >= point_min:
            count_comp_hab += 1

    print(count_comp_hab)


main()
