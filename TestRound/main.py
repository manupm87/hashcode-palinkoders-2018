from definitions import *
from util import util
from pizza import pizzamodule as p
import datetime


"""
R | Number of rows
C | Number of columns
L | Minimum number of each ingredient in a slice
H | Maximum total number of cells of a slice
"""

R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "example.in")
# R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "small.in")
# R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "medium.in")

constraints = {"R": R, "C": C, "L": L, "H": H}

print(constraints)

print()

[print(r) for r in pizza]


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

# av_slices = p.available_slices_for_cell({'r': 0, 'c': 1}, pizza, H, L, R, C, possible_frames=all_slice_frames)
print()
# print(av_slices)
# cell_health = p.cell_health({'r': 0, 'c': 0}, pizza, H, L, R, C)
# print(cell_health)


a = datetime.datetime.now()
health_map = p.compute_health_map(pizza, constraints)
b = datetime.datetime.now()
#[print(r) for r in health_map]
print(b-a)


a = datetime.datetime.now()
health_map = p.compute_health_map(pizza, constraints, possible_frames=all_slice_frames)
b = datetime.datetime.now()
[print(r) for r in health_map]
print(b-a)

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