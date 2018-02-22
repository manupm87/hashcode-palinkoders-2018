from pizza import pizza


def test_possible_frames_of_size_6():
    sol = pizza.possible_slice_frames_of_size(6)
    assert len(sol) is 4
    assert sol.__contains__({'r': 1, 'c': 6})
