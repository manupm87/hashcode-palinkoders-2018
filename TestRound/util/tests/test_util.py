from util import util
from definitions import *


def test_parse_pizza():
    r, c, l, h, pizza = util.parse(INPUT_DATA_DIR + "example.in")
    assert [r, c, l, h] == [3, 5, 1, 6]
    assert pizza.__eq__(["TTTTT", "TMMMT", "TTTTT"])
