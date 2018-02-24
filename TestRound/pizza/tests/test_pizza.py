from definitions import *
import pizza.pizzamodule as p
from util import util


R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "example.in")
constraints = {"R": R, "C": C, "L": L, "H": H}


def test_possible_frames_of_size_6():
    _constraints = {"R": 6, "C": 6, "L": L, "H": H}
    sol = p.get_fitting_frames_of_size(size=6, constraints=_constraints)
    assert len(sol) is 4
    assert sol.__contains__({'r': 1, 'c': 6})


def test_possible_frames_of_size_4():
    _constraints = {"R": 4, "C": 4, "L": L, "H": H}
    sol = p.get_fitting_frames_of_size(size=4, constraints=_constraints)
    assert len(sol) is 3
    assert sol.__contains__({'r': 2, 'c': 2})
    assert sol.__contains__({'r': 4, 'c': 1})


def test_first_slice_of_size_6():
    cut_slice = p.get_ingredients_for_slice_at_pos(pos={"r": 0, "c": 0}, frame={'c': 2, 'r': 3}, pizza=pizza,
                                                   constraints=constraints)
    assert cut_slice.__eq__(['TT', 'TM', 'TT'])


def test_last_slice_of_size_6():
    cut_slice = p.get_ingredients_for_slice_at_pos(pos={"r": 0, "c": 3}, frame={'c': 2, 'r': 3}, pizza=pizza,
                                                   constraints=constraints)
    assert cut_slice.__eq__(['TT', 'MT', 'TT'])


def test_slice_of_size_6_out_of_pizza_bounds():
    cut_slice = p.get_ingredients_for_slice_at_pos(pos={"r": 0, "c": 4}, frame={'c': 2, 'r': 3}, pizza=pizza,
                                                   constraints=constraints)
    assert not cut_slice


def test_not_enough_ingredients_on_slice_full_of_tomato():
    cur_slice = ['TT', 'TT']
    assert not p.is_ingredients_valid(cur_slice, constraints=constraints)


def test_not_enough_ingredients_on_slice_full_of_mushroom():
    cur_slice = ['MM', 'MM']
    assert not p.is_ingredients_valid(cur_slice, constraints=constraints)


def test_enough_ingredients_on_slice_mainly_tomato():
    cur_slice = ['TT', 'MT']
    assert p.is_ingredients_valid(cur_slice, constraints=constraints)


def test_enough_ingredients_on_slice_mainly_mushroom():
    cur_slice = ['MM', 'TM']
    assert p.is_ingredients_valid(cur_slice, constraints=constraints)


def test_slice_with_enough_ingredients_but_overlapping():
    _constraints = {"R": 4, "C": 4, "L": 2, "H": H}
    cur_slice = ['MTT', '*MT', '*MT']
    assert not p.is_ingredients_valid(slice_ingredients=cur_slice, constraints=_constraints)
