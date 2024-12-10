from collections import defaultdict

# # example data
text = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

with open('aoc5.data.txt') as file:
    text = file.read()

# test_str = []

# np_reports = np.array([list(line) for line in text.strip().split('\n')])

output1, output2 = text.split('\n\n')

rules = output1.split('\n')
page_orders = output2.strip().split('\n')
# print(page_orders)

before = defaultdict(list)
after = defaultdict(list)

for rule in rules:
    if rule:
        start, end = rule.split('|')
        after[start].append(end)
        before[end].append(start)

# print(after, before)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

def verify_current(line, current, before, after):
    left, right = current-1, current+1
    test = line[current]
    while left >= 0:
        candidate = line[left]
        # print(candidate, dfs(after, test), after[test])
        # if candidate in dfs(after, test):
        if candidate in after[test]:
            return False
        left -= 1

    while right < len(line):
        candidate = line[right]
        # if candidate not in dfs(before, test):
        if candidate in before[test]:
            return False
        right += 1

    return True

result = 0
for current, line in enumerate(page_orders):
    line = line.split(',')
    # print(line)
    is_valid = []
    for i in range(len(line)):
        is_valid.append(verify_current(line, i, before, after))
        # is_valid.append(verify_current(line, i, before))


    if all(is_valid):
        result += int(line[len(line)//2])

print(result)
