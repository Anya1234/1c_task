import numpy as np


def get_winner_info(cells_centers, image_boolean_data):
    positions = []

    for i in cells_centers:
        figure_type = determine_figure(image_boolean_data, i[0], i[1])
        if figure_type == 'cross':
            positions.append(1)
        if figure_type == 'cycle':
            positions.append(0)
        if figure_type == 'empty':
            positions.append(-1)

    return who_wins(positions)


def who_wins(values):
    table = np.array(values).reshape(3, 3)

    for i in range(3):
        if (table[i] == [0, 0, 0]).all():
            return['zero', 'h', [i*3, i*3+1, i*3+2]]
        if (table[i] == [1, 1, 1]).all():
            return ['cross', 'h', [i * 3, i * 3 + 1, i * 3 + 2]]

    for j in range(3):
        if [table[0][j], table[1][j], table[2][j]] == [0, 0, 0]:
            return['zero', 'v',[j, 3+j, 6+j]]
        if [table[0][j], table[1][j], table[2][j]] == [1, 1, 1]:
            return['cross', 'v', [j, 3+j, 6+j]]

    if [table[0][0], table[1][1], table[2][2]] == [0, 0, 0]:
        return['zero', 'md', [0, 4, 8]]
    if [table[0][0], table[1][1], table[2][2]] == [1, 1, 1]:
        return['cross', 'md', [0, 4, 8]]
    if [table[2][0], table[1][1], table[0][2]] == [0, 0, 0]:
        return['zero', 'sd', [2, 4, 6]]
    if [table[2][0], table[1][1], table[0][2]] == [1, 1, 1]:
        return['cross', 'sd', [2, 4, 6]]

    return "noOne"


def determine_figure(image_data, point, bounds):
    if image_data[point[0]][point[1]]:
        return 'cross'
    else:
        i = point[0]
        while i < bounds[0][1]:
            if image_data[i][point[1]]:
                return 'cycle'
            i += 1
        return 'empty'
