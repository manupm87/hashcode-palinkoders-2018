import math


def get_fitting_frames_of_size(size, constraints):
    """
    Get all frames of size 'size' that fit on the pizza
    :param size:
    :param constraints:
    :return:
    """

    def _get_fitting_frames_of_size(_size, _max_row, _max_col):
        slices = list()
        for i in range(1, int(math.floor(math.sqrt(_size)) + 1)):
            if _size % i == 0:
                cur_slice = {'r': i, 'c': _size // i}
                cur_slice_invert = {'r': _size // i, 'c': i}
                if cur_slice not in slices:
                    if cur_slice['r'] <= _max_row and cur_slice['c'] <= _max_col:
                        slices.append(cur_slice)
                if cur_slice_invert not in slices:
                    if cur_slice_invert['r'] <= _max_row and cur_slice_invert['c'] <= _max_col:
                        slices.append(cur_slice_invert)
        return slices
    return _get_fitting_frames_of_size(size, constraints["R"], constraints["C"])


def get_all_fitting_frames(constraints):
    """
    Get all frames that fit on the pizza
    :param constraints:
    :return:
    """
    def _get_all_fitting_frames(_max_size, _min_ingredients, _max_row, _max_col):
        available_slices = dict()
        for size in range(2 * _min_ingredients, _max_size + 1):
            available_slices[size] = get_fitting_frames_of_size(size=size, constraints=constraints)
        return available_slices
    return _get_all_fitting_frames(constraints["H"], constraints["L"], constraints["R"], constraints["C"])


def get_ingredients_for_slice_at_pos(pos, frame, pizza, constraints):
    """
    Get the slice of pizza with its ingredients
    :param pos:
    :param frame:
    :param pizza:
    :param constraints:
    :return:
    """
    def _get_ingredients_for_slice_at_pos(_pos, _frame, _pizza, _max_rows, _max_cols):
        if not is_valid_pos_for_frame(_pos, _frame, constraints):
            return False
        cur_slice = list()
        for r in range(_frame['r']):
            cur_slice.append(_pizza[_pos['r'] + r][_pos['c']:_pos['c'] + _frame['c']])
        return cur_slice
    return _get_ingredients_for_slice_at_pos(pos, frame, pizza, constraints["R"], constraints["C"])


def is_valid_slice(frame, pos, pizza, constraints):
    """
    Validates whether the slice is valid in terms of position on the pizza, ingredient composition and overlaps.
    :param frame:
    :param pos:
    :param pizza:
    :param constraints:
    :return: True if the slice is valid. False otherwise.
    """
    def _is_valid_slice(_frame, _pos, _pizza, _min_ingredients, _max_rows, _max_cols):
        if not is_valid_pos_for_frame(_frame, _pos, constraints):
            return False
        slice_ingredients = get_ingredients_for_slice_at_pos(_pos, _frame, _pizza, constraints)
        if not is_ingredients_valid(slice_ingredients, constraints):
            return False
        return True
    return _is_valid_slice(frame, pos, pizza, constraints["L"], constraints["R"], constraints["C"])


def is_valid_pos_for_frame(frame, pos, constraints):
    max_rows = constraints["R"]
    max_cols = constraints["C"]
    if pos['r'] + frame['r'] > max_rows or pos['r'] < 0:
        return False
    elif pos['c'] + frame['c'] > max_cols or pos['c'] < 0:
        return False
    else:
        return True


def is_ingredients_valid(slice_ingredients, constraints):
    min_ingredients = constraints["L"]
    count_tomatoes = sum([r.count('T') for r in slice_ingredients])
    count_mushrooms = sum([r.count('M') for r in slice_ingredients])

    return True if not slice_overlaps(slice_ingredients) \
                   and (count_mushrooms >= min_ingredients and count_tomatoes >= min_ingredients) else False


def slice_overlaps(slice_ingredients):
    for r in slice_ingredients:
        for cell in r:
            if cell == '*':
                return True
    return False


def cell_health(cell_pos, pizza, constraints, possible_frames=-1):
    return len(available_slices_for_cell(cell_pos, pizza, constraints, possible_frames))


def frame_positions_containing_cell(cell_pos, slice_shape):
    potential_frame_positions = list()
    for i in range(slice_shape['r']):
        for j in range(slice_shape['c']):
            frame_pos = {'r': cell_pos['r'] - i, 'c': cell_pos['c'] - j}
            potential_frame_positions.append(frame_pos)
    return potential_frame_positions


def available_slices_for_cell(cell_pos, pizza, constraints, possible_frames=-1):
    valid_slices = list()
    if possible_frames == -1:
        all_possible_frames = get_all_fitting_frames(constraints=constraints)
    else:
        all_possible_frames = possible_frames
    for size, frame_shapes in all_possible_frames.items():
        for frame_shape in frame_shapes:
            potential_frame_positions = frame_positions_containing_cell(cell_pos, frame_shape)
            for frame_pos in potential_frame_positions:
                if is_valid_slice(frame_shape, frame_pos, pizza, constraints=constraints):
                    valid_slices.append({"pos": frame_pos, "shape": frame_shape})
    return valid_slices


def compute_health_map(pizza, constraints, possible_frames=-1):
    health_map = list()
    for i, row in enumerate(pizza):
        health_row = list()
        for j, cell in enumerate(row):
            pos = {'r': i, 'c': j}
            health_row.append(cell_health(pos, pizza, constraints, possible_frames))
        health_map.append(health_row)
    return health_map
