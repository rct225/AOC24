reports = []

# # example data
# data = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """

# data = """
# 49 46 45 44 43 40 36
# """

# for line in data.strip().split('\n'):
#     levels = list(map(int, line.split()))
#     reports.append(levels)

with open('aoc2.data.txt') as file:
    for line in file:
        line.strip()
        levels = list(map(int, line.split()))
        reports.append(levels)

def safe(report):
    reading = False
    distances = [current_report - report[i] for i, current_report in enumerate(report[1:])]
    magnitudes = [1 if abs(d) > 0 and abs(d) < 4 else 0 for d in distances]
    if all(item >= 0 for item in distances) or all(item < 0 for item in distances):
        if all(magnitudes):
            reading = True
    return reading



readings = 0
for report in reports:
    readings += safe(report)

print(readings)

readings_b = 0


print(sum(any(safe(report[:i]+report[i+1:]) for i in range(len(report))) for report in reports))
      
