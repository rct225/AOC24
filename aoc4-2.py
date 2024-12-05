import numpy as np

# # example data
text = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

reports = []
# for line in data.strip().split('\n'):
#     levels = list(line)
#     reports.append(levels)


#     for line in file:
#         line.strip()
#         levels = list(line)
#         reports.append(levels)

# np_reports = np.array(reports)

# print(np_reports)

# np_reports = np.fromfile('aoc4.data.txt', dtype='S1')
# with open('aoc4.data.txt') as file:
#     text = file.read()


test_str = []

np_reports = np.array([list(line) for line in text.strip().split('\n')])
test_str.append('\n'.join([''.join(row) for row in np_reports]))

# for row in np_reports:
    # print(''.join(row))


rotated90 = np.rot90(np_reports)
test_str.append('\n'.join([''.join(row) for row in rotated90]))

# for row in rotated90:
#     print(''.join(row))

rotated180 = np.rot90(rotated90)
test_str.append('\n'.join([''.join(row) for row in rotated180]))
# for row in rotated180:
#     print(''.join(row))

rotated270 = np.rot90(rotated180)
test_str.append('\n'.join([''.join(row) for row in rotated270]))

# for row in rotated270:
#     print(''.join(row))

# print(rotated90)
# print(rotated180)
# print(rotated270)



for i in range(-len(np_reports), len(np_reports)):
    current_diagonal = np.diagonal(np_reports, i)
    result = ''.join(current_diagonal)
    test_str.append(result)
    # print(result)

for i in range(-len(np_reports), len(np_reports)):
    current_diagonal = np.diagonal(rotated90, i)
    result = ''.join(current_diagonal)
    test_str.append(result)
    # print(result)

for i in range(-len(np_reports), len(np_reports)):
    current_diagonal = np.diagonal(rotated180, i)
    result = ''.join(current_diagonal)
    test_str.append(result)
    # print(result)

for i in range(-len(np_reports), len(np_reports)):
    current_diagonal = np.diagonal(rotated270, i)
    result = ''.join(current_diagonal)
    test_str.append(result)
    # print(result)


import re

regex = r"XMAS"

trial = ('\n'.join(test_str))

print(trial)

matches = re.findall(regex, trial, re.MULTILINE)

print(len(matches))
