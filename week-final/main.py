import os


def main():
    # Pasta onde ficará os dados
    os.chdir('./work-final/inout-files')
    input_files = filter(lambda x: '.in' in x, os.listdir())

    for file_name in input_files:
        data_file = read_file(file_name)
        matrix, number_str_find, str_find = split_data_test(data_file)
        str_founds = find_words(matrix, str_find)

        new_matrix = set_words_matrix(
            (len(matrix), len(matrix[0])), str_founds)

        write_file(f'{file_name[:len(file_name) - 3]}.res', new_matrix)


def read_file(file_name):
    """ Ler os dados do arquivo.

    Parameters
    -----------
    file_name: str - nome do arquivo.

    Returns
    -----------
    list: matriz contendos os dados lidos.
    """

    data = open(file_name, 'r')
    data_clear = []
    data_line = []

    for char_data in data.read():
        if not(char_data == ' '):
            if char_data == '\n':
                data_clear.append(data_line)
                data_line = []
            else:
                data_line.append(char_data)
    data_clear.append(data_line)

    data.close()

    return data_clear


def write_file(file_name, data):
    """ Cria um arquivo novo com os dados passados.

    Parameters
    -----------
    file_name: str - nome do arquivo a ser criado.\n
    data: list of list (matrix) - matriz de dados.
    """

    new_file = open(file_name, 'w+')

    for data_line in data:
        new_file.write(' '.join(data_line) + '\n')

    new_file.close()


def split_data_test(data_file):
    """ Divide os dados entre, dados de entrada e dados de busca.

    Parameters
    -----------
    data_file: list of list (matrix) - dados de entrada.

    Returns
    -----------
    list: matriz dados de entrada.
    int: quantidade de testes.
    list: matriz dados buscados.
    """

    loop = True
    idx = 0
    while loop and idx < len(data_file):
        loop = not ((data_file[idx][0]).isdigit())
        idx += 1

    return data_file[:idx - 1], int(''.join(data_file[idx - 1])), data_file[idx:]


def find_words(matrix, words_find):
    """ Procura pelas palavras dadas na matriz.

    Parameters
    -----------
    matrix: list of list (matrix) - dados de entrada.\n
    matrix: list of list (matrix) - lista de palavras buscadas.

    Returns
    -----------
    list: retorna os dados das palavras encontradas
        - os dados são: (palavra, posiçãoDeInício, direção).

    """

    shape = (len(matrix), len(matrix[0]))
    words_found = []

    for i in range(shape[0]):
        for j in range(shape[1]):
            for word in words_find:
                result_direction = check_word(matrix, word, (i, j), shape)
                if not (result_direction is None):
                    words_found.append((word, (i, j), result_direction))

    return words_found


def check_word(matrix, word, start_position, shape):
    """ Verifica se a palavra existe a partir de determinada posição.

    Parameters
    -----------
    matrix: list of list (matrix) - dados de entrada.\n
    word: str - palavra buscada.\n
    start_position: tuple - posição de início da busca (linha, coluna).\n

    Returns
    -----------
    tuple or None: or retorna uma tupla se encontrar a palavra, or None caso contrário
    """

    directions_check = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for direction in directions_check:
        i, j, t = start_position[0], start_position[1], 0
        while t < len(word) and 0 <= i < shape[0] and 0 <= j < shape[1] and matrix[i][j] == word[t]:
            i += direction[0]
            j += direction[1]
            t += 1

        if len(word) == t:
            return direction

    return None


def create_matrix(shape):
    """ Cria uma matriz com o tamanho passado e preenche-a com '.'.

    Parameters
    -----------
    shape: tupla - tamanho da matriz (linha, coluna)

    Returns
    -----------
    list: matriz criada
    """

    matrix = [['.' for j in range(shape[1])]
              for i in range(shape[0])]

    return matrix


def set_words_matrix(shape, words):
    """ Adiciona as palavras passada como parâmetro em uma matriz de tamanho passado.

    Parameters
    -----------
    shape: tupla - tamanho da matriz (linha, coluna)\n
    words: list of list (matrix) - lista de palavras

    Returns
    -----------
    list: matriz preenchida com as palavras
    """

    matrix = create_matrix(shape)

    for word in words:
        i, j = word[1][0], word[1][1]
        for t in range(len(word[0])):
            matrix[i][j] = word[0][t]
            i += word[2][0]
            j += word[2][1]

    return matrix


main()
