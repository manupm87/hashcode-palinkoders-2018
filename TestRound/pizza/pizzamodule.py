import math


def possible_slice_frames_of_size(size, max_row, max_col):
    slices = list()
    for i in range(1, int(math.floor(math.sqrt(size)) + 1)):
        if size % i == 0:
            cur_slice = {'r': i, 'c': size // i}
            cur_slice_invert = {'r': size // i, 'c': i}
            if cur_slice not in slices:
                if cur_slice['r'] <= max_row and cur_slice['c'] <= max_col:
                    slices.append(cur_slice)
            if cur_slice_invert not in slices:
                if cur_slice_invert['r'] <= max_row and cur_slice_invert['c'] <= max_col:
                    slices.append( cur_slice_invert)
    return slices


def all_possible_slice_frames(max_size, min_ingredients, max_row, max_col):
    available_slices = dict()
    for size in range(2*min_ingredients, max_size + 1):
        available_slices[size] = possible_slice_frames_of_size(size=size, max_row=max_row, max_col=max_col)
    return available_slices


def slice_at_pos(pos, slice_frame, pizza, max_rows, max_cols):
    if not validate_pos_for_frame(pos, slice_frame, max_rows, max_cols):
        return False
    cur_slice = list()
    for r in range(slice_frame['r']):
        cur_slice.append(pizza[pos['r'] + r][pos['c']:pos['c'] + slice_frame['c']])
    return cur_slice


def validate_pos_for_frame(pos, frame, max_rows, max_cols):
    if pos['r'] + frame['r'] > max_rows or pos['r'] < 0:
        return False
    elif pos['c'] + frame['c'] > max_cols or pos['c'] < 0:
        return False
    else:
        return True


def validate_ingredients_in_slice(slice_ingredients, min_ingredients):
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


def validate_slice(slice_shape, slice_pos, pizza, min_ingredients, max_rows, max_cols):
    if not validate_pos_for_frame(slice_pos, slice_shape, max_rows, max_cols):
        return False
    slice_ingredients = slice_at_pos(slice_pos, slice_shape, pizza, max_rows, max_cols)
    if not validate_ingredients_in_slice(slice_ingredients, min_ingredients):
        return False
    return True


def filter_invalid_slices(slice_shape, slices_positions, pizza, min_ingredients, max_rows, max_cols):
    valid_slices = list()
    for slice_pos in slices_positions:
        if validate_slice(slice_shape, slice_pos, pizza, min_ingredients, max_rows, max_cols):
            valid_slices.append(slice_pos)
    return valid_slices


def cell_health(cell_pos, pizza, max_size, min_ingredients, max_rows, max_cols):
    return len(available_slices_for_cell(cell_pos, pizza, max_size, min_ingredients, max_rows, max_cols))


def frame_positions_containing_cell(cell_pos, slice_shape):
    potential_frame_positions = list()
    for i in range(slice_shape['r']):
        for j in range(slice_shape['c']):
            frame_pos = {'r': cell_pos['r'] - i, 'c': cell_pos['c'] - j}
            potential_frame_positions.append(frame_pos)
    return potential_frame_positions


def available_slices_for_cell(cell_pos, pizza, max_size, min_ingredients, max_rows, max_cols):
    valid_slices = list()
    all_possible_frames = all_possible_slice_frames(max_size, min_ingredients, max_rows, max_cols)
    for size, frame_shapes in all_possible_frames.items():
        for frame_shape in frame_shapes:
            potential_frame_positions = frame_positions_containing_cell(cell_pos, frame_shape)
            for frame_pos in potential_frame_positions:
                if validate_slice(frame_shape, frame_pos, pizza, min_ingredients, max_rows, max_cols):
                    valid_slices.append({"pos": frame_pos, "shape": frame_shape})
    return valid_slices
