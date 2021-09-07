import re

fname = input('Enter file:')
if len(fname) < 1:
    fname = "regex_sum_42.txt"

hand = open(fname)
nums = list()

for line in hand:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    for item in num:
        item_num = int(item)
        nums.append(item_num)

print(nums)
print(len(nums))
print(sum(nums))
