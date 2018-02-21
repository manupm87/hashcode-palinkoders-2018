def parse(file_path):
    with open(file_path) as f:
        R, C, L, H = map(int, f.readline().split())
        pizza = list()
        for r in range(R):
            pizza.append(f.readline().strip())

    f.close()

    return [R, C, L, H, pizza]
