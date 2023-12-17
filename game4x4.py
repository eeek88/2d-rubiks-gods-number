import copy

M = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]

matrices_set = set()
matrices_set.add(tuple(map(tuple, M)))


def rotation(i, j, matrix):
    matrix_bak = copy.deepcopy(matrix)

    matrix[0 + i][0 + j] = matrix_bak[1 + i][0 + j]  # rotation assignments
    matrix[0 + i][1 + j] = matrix_bak[0 + i][0 + j]
    matrix[1 + i][0 + j] = matrix_bak[1 + i][1 + j]
    matrix[1 + i][1 + j] = matrix_bak[0 + i][1 + j]

    return matrix


def generate_positions(matrix):
    rotations = []
    for i in range(3):
        for j in range(3):
            rotated_matrix = rotation(i, j, copy.deepcopy(matrix))
            rotations.append(rotated_matrix)
    return rotations

num_positions = 0

while len(matrices_set) <= 63063000:
    num_positions += 1
    print(len(matrices_set))

    new_matrices = set() 
    for matrix_tuple in matrices_set:
        matrix = [list(row) for row in matrix_tuple]  # convert tuple back to list
        new_games = generate_positions(matrix)
        for new_matrix in new_games:
            new_matrices.add(tuple(map(tuple, new_matrix)))

    matrices_set.update(new_matrices)

with open('games.txt', 'w') as file:
    for matrix_tuple in new_matrices:
        matrix = [list(row) for row in matrix_tuple] # convert back to list
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
        file.write('\n') 

