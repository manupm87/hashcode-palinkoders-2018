def parse(file_path):
    with open(file_path) as f:
        r, c, l, h = map(int, f.readline().split())
        pizza = list()
        for row in range(r):
            pizza.append(f.readline().strip())

    f.close()

    return [r, c, l, h, pizza]
