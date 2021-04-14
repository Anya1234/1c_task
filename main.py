from PIL import Image, ImageDraw
import numpy as np
from parse_image import find_centers, find_black
from find_winner import get_winner_info

print("Write path to file with image:")

image = Image.open(input())

print("Write path to result file with image:")

result_path = input()

data = np.asarray(image)

boolean_data = find_black(data)

cells_centers = find_centers(boolean_data)

winner_info = get_winner_info(cells_centers, boolean_data)

if winner_info == "noOne":
    print("No one wins")
else:
    print("\nWins person who plays for " + winner_info[0])
    print("\n------------------------------------------\n")
    print("result is written to" + result_path + "result.png file\n")
    cells_centers[winner_info[2][0]][0].reverse()
    cells_centers[winner_info[2][2]][0].reverse()
    to_draw=[tuple(cells_centers[winner_info[2][0]][0]),
             tuple(cells_centers[winner_info[2][2]][0])]

    drawer = ImageDraw.Draw(image)
    drawer.line(to_draw, fill='black', width=10)

    image.save(result_path, "PNG")