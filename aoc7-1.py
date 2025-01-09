# # example

from itertools import chain, zip_longest
import math


text = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

#     # for line in file:
#     #     line.strip()
#     #     levels = list(line)
#     #     reports.append(levels)



with open('aoc7.data.txt') as file:
    text = file.read()

reports = []
for line in text.strip().split('\n'):
    # levels = list(line)
    reports.append(line)

# np_reports = np.array(reports)

# print(np_reports)

addition = lambda a,b: a+b
multiplication = lambda a,b: a*b
operators = [addition, multiplication]


def evaluate(values: list, testValue: int):
    if(len(values) == 1): 
        return values[0] == testValue
    for op in operators:
        value = op(values[0], values[1])
        if(evaluate([value] + values[2::], testValue)):
            return True
    return False


total = 0
for rep in reports:
    result, values = rep.split(':')
    values = list(map(int, values.split()))
    result = int(result)
    # expr = []
    # mods = [int(result) % v for v in values]
    # ops = []
    # for i in range(len(mods)-1):
    #     if mods[i] == mods[i+1]:
    #         ops += ["*"]
    #         i += 1
    #     else:

    #         ops += ["+"]
    # print(ops)
    # print(values)
    # print(result)

    # print(evaluate(values,result))
    if evaluate(values,result):
        total += result

print(total)