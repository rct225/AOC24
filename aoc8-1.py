import itertools
import math
from matplotlib import pyplot as plt
import numpy as np

# # example

text = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

with open('aoc8.data.txt') as file:
    text = file.read()

reports = []
for line in text.strip().split('\n'):
    levels = list(line)
    reports.append(levels)

np_reports = np.array(reports)
# print(np_reports.shape)

# print(np_reports)

def new_point_on_line(p, q, distance):
    """Finds a new point along the line defined by (x1, y1) and (x2, y2) at a given distance from (x1, y1)."""

    # Calculate the length of the line segment
    length = math.dist(p, q)

    x1, x2 = p[0], q[0]
    y1, y2 = p[1], q[1]

    # # Calculate the unit vector in the direction of the line
    # unit_x = (x2 - x1) / length
    # unit_y = (y2 - y1) / length

    # Calculate the new point's coordinates
    new_x = x2 + (x2 - x1)
    new_y = y2 + (y2 - y1)

    return int(new_x), int(new_y)

freqs = set(np_reports[np_reports != '.'])

pt = []
for i, freq in enumerate(freqs):
    points = np.array(np.where(np_reports == freq)).T
    for combination in itertools.combinations(points, 2):
        p = combination[0]
        q = combination[1]
        distance = math.dist(p, q)  
        # print(p, q, distance)
        p1 = new_point_on_line(p, q, distance * 2)
        pt += [p1]
        # print(p1)
        p2 = new_point_on_line(q, p, distance * 2)
        pt += [p2]
        # print(p2)
        # pt[(x, y)] = freq

# print(pt, len(pt))

filtered_pt = [(x,y) for x, y in pt if x < np_reports.shape[0] and y < np_reports.shape[1] and x >= 0 and y >= 0]
# print(filtered_pt, len(filtered_pt))
# print(set(filtered_pt), len(set(filtered_pt)))
print(len(set(filtered_pt)))
# print(set(pt), len(set(pt)))