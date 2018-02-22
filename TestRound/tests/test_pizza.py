from pizza import pizza as p
from util import util


R, C, L, H, pizza = util.parse("../input_data/example.in")


def test_possible_frames_of_size_6():
    sol = p.possible_slice_frames_of_size(size=6)
    assert len(sol) is 4
    assert sol.__contains__({'r': 1, 'c': 6})


def test_first_slice_of_size_6():
    cut_slice = p.slice_at_pos(pos={"r": 0, "c": 0}, slice_frame={'c': 2, 'r': 3}, pizza=pizza)
    assert cut_slice.__eq__(['TT', 'TM', 'TT'])


def test_last_slice_of_size_6():
    cut_slice = p.slice_at_pos(pos={"r": 0, "c": 3}, slice_frame={'c': 2, 'r': 3}, pizza=pizza)
    assert cut_slice.__eq__(['TT', 'MT', 'TT'])


def test_slice_of_size_6_out_of_pizza_bounds():
    cut_slice = p.slice_at_pos(pos={"r": 0, "c": 4}, slice_frame={'c': 2, 'r': 3}, pizza=pizza)
    assert not cut_slice


def test_not_enough_ingredients_on_slice_full_of_tomato():
    cur_slice = ['TT', 'TT']
    assert not p.validate_ingredients_in_slice(cur_slice, 1)


def test_not_enough_ingredients_on_slice_full_of_mushroom():
    cur_slice = ['MM', 'MM']
    assert not p.validate_ingredients_in_slice(cur_slice, 1)


def test_enough_ingredients_on_slice_mainly_tomato():
    cur_slice = ['TT', 'MT']
    assert p.validate_ingredients_in_slice(cur_slice, 1)


def test_enough_ingredients_on_slice_mainly_mushroom():
    cur_slice = ['MM', 'TM']
    assert p.validate_ingredients_in_slice(cur_slice, 1)

