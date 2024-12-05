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

def item_count(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

right_count = item_count(right)

similairity = [l * right_count.get(l, 0) for l in left]

print(sum(similairity))

