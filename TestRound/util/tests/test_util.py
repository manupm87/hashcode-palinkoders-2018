from util import util


def test_parse_pizza():
    r, c, l, h, pizza = util.parse("input_data/example.in")
    assert [r, c, l, h] == [3, 5, 1, 6]
    assert pizza.__eq__(["TTTTT", "TMMMT", "TTTTT"])
