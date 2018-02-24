import random
from definitions import *


def parse(file_path):
    with open(file_path) as f:
        r, c, l, h = map(int, f.readline().split())
        pizza = list()
        for row in range(r):
            pizza.append(f.readline().strip())

    f.close()

    return [r, c, l, h, pizza]


def generate_input_data(file_name, rows, cols, L, H):
    ingredients = ['T', 'M']

    with open(INPUT_DATA_DIR + file_name + ".in", 'w') as f:
        f.write("{} {} {} {}\n".format(rows, cols, L, H))
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(random.choice(ingredients))
            f.write("".join(row) + "\n")
    f.close()
