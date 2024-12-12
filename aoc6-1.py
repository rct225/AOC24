import matplotlib.pyplot as plt
import numpy as np
import heapq

# # example

# text = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """

# reports = []
# for line in text.strip().split('\n'):
#     levels = list(line)
#     reports.append(levels)


#     # for line in file:
#     #     line.strip()
#     #     levels = list(line)
#     #     reports.append(levels)



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


rows, cols = warehouse.shape
# print(rows, cols)
current = start
visted = set()
while True:
    visted.add(current)
    # is current out of bounds
    # if current[0] < 0 or current[0] >= rows or current[1] < 0 or current[1] >= cols:
    #     break
    next = tuple(np.array(current) + np.array(movements_map[direction]))
    if next[0] < 0 or next[0] >= rows or next[1] < 0 or next[1] >= cols:
        break
    if warehouse[next] == 1:
         direction = get_direction(direction)
    else:
         current = next
    # print(current)

print(len(visted))
        



