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

R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "example.in")
#R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "small.in")
# R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "medium.in")

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
print(all_slice_frames)


"""
For each cell, calculate its 'health'
'cell health' = number of slice_frames on which could fit (can only fit if the constraints are met)
"""
# frame = {'c': 2, 'r': 2}
# frame_positions = p.frame_positions_containing_cell(cell_pos={'r': 1, 'c': 1}, slice_shape=frame)
# print(frame_positions)

av_slices = p.available_slices_for_cell({'r': 0, 'c': 1}, pizza, constraints, possible_frames=all_slice_frames)
print()
print(json.dumps(av_slices, indent=4))
# get_cell_health = p.get_cell_health({'r': 0, 'c': 0}, pizza, H, L, R, C)
# print(get_cell_health)


a = datetime.datetime.now()
health_map = p.compute_health_map(pizza, constraints)
b = datetime.datetime.now()
#[print(r) for r in health_map]
print(b-a)


a = datetime.datetime.now()
health_map = p.compute_health_map(pizza, constraints, possible_frames=all_slice_frames)
b = datetime.datetime.now()
[print("\t".join(map(str, r))) for r in health_map]
print(b-a)

next_cell = p.get_cell_pos_with_minimum_health(health_map)
print(next_cell)

pizza_slice = {'r0': 0, 'c0': 2,
               'r1': 2, 'c1': 4}

slice_neighbors = p.get_neighbor_cells_for_slice(pizza_slice, pizza, constraints)
print(slice_neighbors)

neighbors_health = p.get_neighbor_cells_health(pizza_slice, pizza, health_map, constraints)
print(neighbors_health)

print("Compute best slice for (0,0)")
cell = {'r': 0, 'c': 0}
best_slice = p.get_best_slice_for_cell_at_pos(cell, pizza, health_map, constraints)
print(best_slice)

p.cut_slice(best_slice, pizza, health_map)
[print("\t".join(r)) for r in pizza]
print()
[print("\t".join(map(str, r))) for r in health_map]

"""
# While there is any cell with health bigger than 0:
# Grab the cell with smallest health and cut the pizza with a slice containing the cell.
# The slice should be selected in a way that maximizes the min(health) of the surrounding cells.
# When the slice is selected, update the pizza and health maps
# (if wanna save resources, update only cells close / adjacent / none)
"""


"""
Write output
"""


"""
Validate output
"""


"""
Calculate points
"""


"""
Calculate algorithm performance (TOTAL_POINTS / PIZZA SIZE)
"""