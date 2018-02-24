import math
import sys


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


def get_cell_health(cell_pos, pizza, constraints, possible_frames=-1):
    return len(available_slices_for_cell(cell_pos, pizza, constraints, possible_frames))


def frame_positions_containing_cell(cell_pos, slice_shape):
    potential_frame_positions = list()
    for i in range(slice_shape['r']):
        for j in range(slice_shape['c']):
            frame_pos = {'r': cell_pos['r'] - i, 'c': cell_pos['c'] - j}
            potential_frame_positions.append(frame_pos)
    return potential_frame_positions


def available_slices_for_cell(cell_pos, pizza, constraints, possible_frames=-1):
    """
    Get all the slices that the cell at 'cell_pos' can be part of.
    :param cell_pos:
    :param pizza:
    :param constraints:
    :param possible_frames:
    :return:
    """

    valid_slices = list()

    # Return empty list if checking a void cell
    if pizza[cell_pos['r']][cell_pos['c']] == '*':
        return valid_slices

    if possible_frames == -1:
        all_possible_frames = get_all_fitting_frames(constraints=constraints)
    else:
        all_possible_frames = possible_frames
    for size, frame_shapes in all_possible_frames.items():
        for frame_shape in frame_shapes:
            potential_frame_positions = frame_positions_containing_cell(cell_pos, frame_shape)
            for frame_pos in potential_frame_positions:
                if is_valid_slice(frame_shape, frame_pos, pizza, constraints=constraints):
                    valid_slice = {'r0': frame_pos['r'],
                                   'c0': frame_pos['c'],
                                   'r1': frame_pos['r'] + frame_shape['r'] - 1,
                                   'c1': frame_pos['c'] + frame_shape['c'] - 1}
                    valid_slices.append(valid_slice)

    return valid_slices


def compute_health_map(pizza, constraints, possible_frames=-1):
    health_map = list()
    for i, row in enumerate(pizza):
        health_row = list()
        for j, cell in enumerate(row):
            pos = {'r': i, 'c': j}
            health_row.append(get_cell_health(pos, pizza, constraints, possible_frames))
        health_map.append(health_row)
    return health_map


def get_cell_pos_with_minimum_health(health_map):
    cell_health = sys.maxsize
    cell_pos = {'r': -1, 'c': -1}
    for r, row in enumerate(health_map):
        for c, health in enumerate(row):
            if 0 < health < cell_health:
                cell_health = health
                cell_pos = {'r': r, 'c': c}
                if cell_health == 1:
                    return cell_pos
    if cell_health == sys.maxsize:
        return False
    return cell_pos


def get_neighbor_cells_for_slice(pizza_slice, pizza, constraints):

    neighbors = list()

    upper_neighbors = [{"r": pizza_slice["r0"] - 1, "c": c} for c in range(pizza_slice["c0"], pizza_slice["c1"] + 1) if
                       pizza_slice["r0"] - 1 >= 0 and pizza[pizza_slice["r0"] - 1][c] != '*']

    bottom_neighbors = [{"r": pizza_slice["r1"] + 1, "c": c} for c in range(pizza_slice["c0"], pizza_slice["c1"] + 1) if
                        pizza_slice["r1"] + 1 < constraints["R"] and pizza[pizza_slice["r1"] + 1][c] != '*']

    left_neighbors = [{"r": r, "c": pizza_slice["c0"] - 1} for r in range(pizza_slice["r0"], pizza_slice["r1"] + 1) if
                      pizza_slice["c0"] - 1 >= 0 and pizza[r][pizza_slice["c0"] - 1] != '*']

    right_neighbors = [{"r": r, "c": pizza_slice["c1"] + 1} for r in range(pizza_slice["r0"], pizza_slice["r1"] + 1) if
                       pizza_slice["c1"] + 1 < constraints["C"] and pizza[r][pizza_slice["c1"] + 1] != '*']

    neighbors.extend(upper_neighbors)
    neighbors.extend(bottom_neighbors)
    neighbors.extend(left_neighbors)
    neighbors.extend(right_neighbors)

    return neighbors


def get_neighbor_cells_health(pizza_slice, pizza, health_map, constraints):
    neighbors = get_neighbor_cells_for_slice(pizza_slice, pizza, constraints)
    neighbors_health = [health_map[n["r"]][n["c"]] for n in neighbors]
    return neighbors_health


def get_slice_score(pizza_slice, pizza, health_map, constraints):
    neighbors_health = get_neighbor_cells_health(pizza_slice, pizza, health_map, constraints)
    if len(neighbors_health) == 0:
        return 1
    else:
        min_health = min([h for h in neighbors_health if h >= 0])
        score = min_health
        return score


def get_best_slice_for_cell_at_pos(pos, pizza, health_map, constraints):
    possible_slices = available_slices_for_cell(pos, pizza, constraints)
    if len(possible_slices) == 0:
        return -1
    # cur_best_slice = possible_slices[0]
    # cur_score = get_slice_score(cur_best_slice, pizza, health_map, constraints)
    best_slice = max(possible_slices, key=lambda x: get_slice_score(x, pizza, health_map, constraints))
    return best_slice


def cut_slice(pizza_slice, pizza, health_map):
    for r in range(pizza_slice["r0"], pizza_slice["r1"] + 1):
        for c in range(pizza_slice["c0"], pizza_slice["c1"] + 1):
            pizza[r][c] = "*"
            health_map[r][c] = -1
    return pizza
