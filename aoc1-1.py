# example data
# left = [3, 4, 2, 1, 3, 3]
# right = [4, 3, 5, 3, 9, 3]

left = []
right = []

with open('aoc1.data.txt') as file:
    for line in file:
        if line.strip() and not line.startswith('#'):
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)

left_sort = sorted(left)
right_sort = sorted(right)

distance = [abs(l - r) for l, r in zip(left_sort, right_sort)]

print(sum(distance))
