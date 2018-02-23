from util import util


def test_parse_pizza():
    R, C, L, H, pizza = util.parse("input_data/example.in")
    assert [R, C, L, H] == [3, 5, 1, 6]
    assert pizza.__eq__(["TTTTT", "TMMMT", "TTTTT"])


