import matplotlib.pyplot as plt
import numpy as np
import heapq

# # example

text = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

with open('aoc6.data.txt') as file:
    text = file.read()

reports = []
for line in text.strip().split('\n'):
    levels = list(line)
    reports.append(levels)

np_reports = np.array(reports)

# print(np_reports)
# print(np_reports)
start = tuple(int(i[0]) for i in np.where(np_reports == '^'))


np_reports[np_reports == '^'] = int(0)
np_reports[np_reports == '.'] = int(0)
np_reports[np_reports == '#'] = int(1)

# test_block = (6,3)
# np_reports[test_block] = 1

warehouse = np_reports.astype(int)

# print(warehouse, start)

movements_map = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

direction = "up"

def get_direction(direction):
        if direction == 'up':
            return 'right'
        elif direction == 'right':
            return 'down'
        elif direction == 'down':
            return 'left'
        elif direction == 'left':
            return 'up'

def walk(warehouse, start, direction='up'):
    rows, cols = warehouse.shape
    current = start
    visted = set()
    history = set()
    history.add((current, direction))
    while True:
        visted.add(current)
        next = tuple(np.array(current) + np.array(movements_map[direction]))
        if next[0] < 0 or next[0] >= rows or next[1] < 0 or next[1] >= cols:
            break
        if warehouse[next] == 1:
            direction = get_direction(direction)
        else:
            current = next
        new_entry = (current, direction)
        if new_entry in history:
            raise InfiniteLoopError
        history.add(new_entry)

    return visted
#part1

visited = walk(warehouse, start)
print(len(walk(warehouse, start)))

class InfiniteLoopError(Exception):
    """raised when the guard stays on the grid infinitely"""

loops = 0
for v in visited:
    mod_warehouse = warehouse.copy()
    mod_warehouse[v] = 1
    try:
        test = walk(mod_warehouse, start)
    except InfiniteLoopError:
        loops += 1

print(loops)


# blocks = [i for i in np.argwhere(warehouse == 1)]

# print(blocks)
# print(turns)

# def find_rect(p1, p2, p3):

#     x4 = p1[1][0] + p3[1][0] - p2[1][0]
#     y4 = p1[1][1] + p3[1][1] - p2[1][1]
#     return (x4, y4)

# # p0 = start

# print(len(turns))
# for i in range(0, len(turns), 3):
#     print(i)
#     if i >= len(turns)-1:
#         break
#     p0, p1, p2 = turns[i:i+3]
#     print(p0, p1, p2)
#     p3 = find_rect(p0, p1, p2)
#     print(np.array(p3) + np.array(movements_map[p2[0]]))


# p0, p1, p2 = turns[0:3]

# print(p0, p1, p2)

# p3 = find_rect(p0, p1, p2)

# print(np.array(p3) + np.array(movements_map[p2[0]]))

# print(p2[0])


