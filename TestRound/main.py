from definitions import *
from util import util


"""
R | Number of rows
C | Number of columns
L | Minimum number of each ingredient in a slice
H | Maximum total number of cells of a slice
"""

R, C, L, H, pizza = util.parse(INPUT_DATA_DIR + "small.in")

print([R, C, L, H])

print(pizza)

# Get all the available slice_frames for the current set up (it depends on L & H) (to be on the safe side, there should
# not be slice_frames with any dimension bigger than the pizza.


# For each cell, calculate its 'health'
# 'cell health' = number of slice_frames on which could fit (can only fit if the constraints are met)


# While there is any cell with health bigger than 0:
# Grab the cell with smallest health and cut the pizza with a slice containing the cell.
# The slice should be selected in a way that maximizes the min(health) of the surrounding cells.
# When the slice is selected, update the pizza and health maps
# (if wanna save resources, update only cells close / adjacent / none)


# Write output


# Validate output


# Calculate points


# Calculate algorithm performance (TOTAL_POINTS / PIZZA SIZE)