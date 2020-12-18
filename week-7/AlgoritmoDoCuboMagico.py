def main():

    move_tokens = input().split(' ')
    move_reverse_token = []

    for move in move_tokens:
        if len(move) == 1:
            move_reverse_token.append(move + '\'')
        else:
            move_reverse_token.append((move if move[1] == '2' else move[0]))

    print(move_reverse_token[len(move_reverse_token) - 1], end='')
    for i in range(len(move_reverse_token) - 2, -1, -1):
        print(f' {move_reverse_token[i]}', end='')
    print()


main()
