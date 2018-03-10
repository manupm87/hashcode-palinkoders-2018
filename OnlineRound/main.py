from definitions import *
from util import util

file_name = "dummy_example"

R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + file_name + ".in")
[print("\t".join(r)) for r in pizza]
