# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
# import math

regex = r"mul\((\d+),(\d+)\)"

# # test_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open('aoc3.data.txt') as file:
    s = file.read()

matches = re.finditer(regex, s, re.MULTILINE)

total = 0
for match in matches:
    # print(match)
    # print(match.group(1), match.group(2))
    total += int(match.group(1)) * int(match.group(2))
print(total)