from definitions import *
from util import util
from pizza import pizzamodule as p
import datetime
import json


"""
R | Number of rows
C | Number of columns
L | Minimum number of each ingredient in a slice
H | Maximum total number of cells of a slice
"""

file_name = "example"
file_name = "custom_example"
file_name = "small"
file_name = "random_input_20_20"
file_name = "random_input_25_25"
file_name = "random_input_30_30"
#file_name = "medium"

R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + file_name + ".in")

constraints = {"R": R, "C": C, "L": L, "H": H}
pizza = [list(row) for row in pizza]
print(constraints)

print()

[print("\t".join(r)) for r in pizza]


"""
Get all the available slice_frames for the current set up (it depends on L & H) (to be on the safe side, 
there should not be slice_frames with any dimension bigger than the pizza.
"""
all_slice_frames = p.get_all_fitting_frames(constraints)
# print(all_slice_frames)


"""
For each cell, calculate its 'health'
'cell health' = number of slice_frames on which could fit (can only fit if the constraints are met)
"""

a = datetime.datetime.now()
health_map = p.compute_health_map(pizza, constraints, possible_frames=all_slice_frames)
b = datetime.datetime.now()
[print("\t".join(map(str, r))) for r in health_map]
print(b-a)


"""
# While there is any cell with health bigger than 0:
# Grab the cell with smallest health and cut the pizza with a slice containing the cell.
# The slice should be selected in a way that maximizes the min(health) of the surrounding cells.
# When the slice is selected, update the pizza and health maps
# (if wanna save resources, update only cells close / adjacent / none)
"""
slices = list()

next_cell = p.get_cell_pos_with_minimum_health(health_map)

while next_cell:
    best_slice = p.get_best_slice_for_cell_at_pos(next_cell, pizza, health_map, constraints)
    # print(best_slice)
    if best_slice == -1:
        # Recalculate health_map
        health_map = p.compute_health_map(pizza, constraints, possible_frames=all_slice_frames)
        next_cell = p.get_cell_pos_with_minimum_health(health_map)
        continue
    slices.append(best_slice)

    p.cut_slice(best_slice, pizza, health_map)

    #health_map = p.compute_health_map(pizza, constraints, possible_frames=all_slice_frames)

    if R * C <= 1000:
        print("\n------------------------------------\n")
        [print("\t".join(r)) for r in pizza]
        print()
        [print("\t".join(map(str, r))) for r in health_map]

    next_cell = p.get_cell_pos_with_minimum_health(health_map)

"""
Write output
"""
with open(OUTPUT_DATA_DIR + file_name + ".out", 'w') as f:
    f.write(str(len(slices)) + "\n")
    for s in slices:
        f.write("{} {} {} {}\n".format(s["r0"], s["c0"], s["r1"], s["c1"]))

f.close()

"""
Validate output
"""


"""
Calculate points
"""
used_ingredients = sum([r.count('*') for r in pizza])


"""
Calculate algorithm performance (TOTAL_POINTS / PIZZA SIZE)
"""

max_ingredients = R * C

ratio = 100 * used_ingredients / max_ingredients

print("\n{}% of the pizza was delivered!".format(ratio))
