import numpy as np


def find_black(image_data):
    print(image_data)
    result = np.full((image_data.shape[0], image_data.shape[1]), False)
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            if image_data[i][j][0] < 50 and image_data[i][j][1] < 50 and \
                    image_data[i][j][2] < 50 and image_data[i][j][3] > 100:
                result[i][j] = True
    return result


def find_coordinates(image_data):
    cnt = 0
    upper_result = np.full((2, 2, 2), 0)
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            if cnt > 1:
                break
            if cnt == 1 and j <= upper_result[0][1][1]:
                continue
            if image_data[i][j]:
                upper_result[cnt][0] = [i, j]
                while image_data[i][j]:
                    j += 1
                upper_result[cnt][1] = [i, j - 1]
                cnt += 1
                if cnt > 1:
                    break

    cnt = 0
    lower_result = np.full((2, 2, 2), 0)
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            if cnt > 1:
                break
            if cnt == 1 and j <= lower_result[0][1][1]:
                continue
            if image_data[image_data.shape[0] - i - 1][j]:
                lower_result[cnt][0] = [image_data.shape[0] - i - 1, j]
                while image_data[image_data.shape[0] - i - 1][j]:
                    j += 1
                lower_result[cnt][1] = [image_data.shape[0] - i - 1, j - 1]
                cnt += 1
                if cnt > 1:
                    break

    cnt = 0
    left_result = np.full((2, 2, 2), 0)
    for j in range(image_data.shape[1]):
        for i in range(image_data.shape[0]):
            if cnt > 1:
                break
            if cnt == 1 and i <= left_result[0][1][0]:
                continue
            if image_data[i][j]:
                left_result[cnt][0] = [i, j]
                while image_data[i][j]:
                    i += 1
                left_result[cnt][1] = [i - 1, j]
                cnt += 1
                if cnt > 1:
                    break

    cnt = 0
    right_result = np.full((2, 2, 2), 0)
    for j in range(image_data.shape[1]):
        for i in range(image_data.shape[0]):
            if cnt > 1:
                break
            if cnt == 1 and i <= right_result[0][1][0]:
                continue
            if image_data[i][image_data.shape[1] - j - 1]:
                right_result[cnt][0] = [i, image_data.shape[1] - j - 1]
                while image_data[i][image_data.shape[1] - j - 1]:
                    i += 1
                right_result[cnt][1] = [i - 1, image_data.shape[1] - j - 1]
                cnt += 1
                if cnt > 1:
                    break

    return {"upper": upper_result,
            "lower": lower_result,
            "lefter": left_result,
            "righter": right_result}


def find_centers(image_boolean_data):
    coordinates = find_coordinates(image_boolean_data)
    centers = []
    x_bounds = []
    y_bounds = []
    horizontals = np.full(3, 0)
    vertical = np.full(3, 0)

    vertical[0] = (coordinates['upper'][0][0][0] + coordinates['lefter'][0][0][0]) / 2
    vertical[1] = (coordinates['lefter'][0][1][0] + coordinates['lefter'][1][0][0]) / 2
    vertical[2] = (coordinates['lower'][0][0][0] + coordinates['lefter'][1][1][0]) / 2

    x_bounds.append([coordinates['upper'][0][0][0], coordinates['lefter'][0][0][0]])
    x_bounds.append([coordinates['lefter'][0][1][0], coordinates['lefter'][1][0][0]])
    x_bounds.append([coordinates['lefter'][1][1][0], coordinates['lower'][0][0][0]])

    horizontals[0] = (coordinates['upper'][0][0][1] + coordinates['lefter'][0][0][1]) / 2
    horizontals[1] = (coordinates['upper'][0][1][1] + coordinates['upper'][1][0][1]) / 2
    horizontals[2] = (coordinates['upper'][1][1][1] + coordinates['righter'][0][0][1]) / 2

    y_bounds.append([coordinates['lefter'][0][0][1], coordinates['upper'][0][0][1]])
    y_bounds.append([coordinates['upper'][0][1][1], coordinates['upper'][1][0][1]])
    y_bounds.append([coordinates['upper'][1][1][1], coordinates['righter'][0][0][1]])

    for i in range(3):
        for j in range(3):
            centers.append([[vertical[i], horizontals[j]], [x_bounds[i], y_bounds[j]]])

    return centers
