import numpy as np

# # example data
# text = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """

with open('aoc4.data.txt') as file:
    text = file.read()

test_str = []

np_reports = np.array([list(line) for line in text.strip().split('\n')])

test_mask = np.array([
    ["M", "1", "S"], ["1", "A", "1"], ["M", "1", "S"]
])

generic_mask = np.array([
    ["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]
])

t2 = np.equal(test_mask, generic_mask)

temp_reports = np_reports.copy()

count = 0
for i in range(4):
    for r in range(1,np.shape(temp_reports)[0]-1):
        for c in range(1,np.shape(temp_reports)[0]-1):
            test = temp_reports[r-1:r+2, c-1:c+2]
            check = np.equal(test, test_mask)
            # print((check == t2).all())
            # print(type(check))
            # print(check, "\n", b_mask)
            if (check == t2).all():
                # print(f'Found at {r},{c}')
                count += 1
            # print(test)
            # print('---')
    temp_reports = np.rot90(temp_reports)

print(count)