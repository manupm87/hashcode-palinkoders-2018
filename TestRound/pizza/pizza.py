from util import util

R, C, L, H, pizza = util.parse("../input_data/example.in")


def possible_slice_frames_of_size(area):
    slices = list()
    slices.extend([{'r': 1, 'c': area}, {'r': area, 'c': 1}])
    for i in range(2, area // 2):
        if area % i == 0:
            slices.extend([{'r': i, 'c': area // i}, {'r': area // i, 'c': i}])
    return slices


def slice_at_pos(pos, slice_frame, pizza):
    if validate_pos_for_frame(pos, slice_frame, pizza) < 0:
        return False
    cur_slice = list()
    for r in range(slice_frame['r']):
        cur_slice.append(pizza[pos['r'] + r][pos['c']:pos['c'] + slice_frame['c']])
    return cur_slice


def validate_pos_for_frame(pos, frame, pizza):
    rows = len(pizza)
    columns = len(pizza[0])

    if pos['r'] + frame['r'] > rows:
        return -1
    elif pos['c'] + frame['c'] > columns:
        return -2
    else:
        return 0


def validate_ingredients_in_slice(pizza_slice, min_ingredients):
    count_tomatoes = sum([r.count('T') for r in pizza_slice])
    count_mushrooms = sum([r.count('M') for r in pizza_slice])
    return True if (count_mushrooms >= min_ingredients and count_tomatoes >= min_ingredients) else False



# Refactor into tests from here

print([R, C, L, H])
print(pizza)

print(possible_slice_frames_of_size(H))

print(slice_at_pos(pos={"r": 0, "c": 0}, slice_frame={'c': 2, 'r': 3}, pizza=pizza))
print(slice_at_pos(pos={"r": 0, "c": 3}, slice_frame={'c': 2, 'r': 3}, pizza=pizza))
print(slice_at_pos(pos={"r": 0, "c": 4}, slice_frame={'c': 2, 'r': 3}, pizza=pizza))

print(validate_ingredients_in_slice(['TT', 'TT'], 1))
print(validate_ingredients_in_slice(['MM', 'MM'], 1))
print(validate_ingredients_in_slice(['TT', 'MT'], 1))
print(validate_ingredients_in_slice(['MT', 'MM'], 1))
