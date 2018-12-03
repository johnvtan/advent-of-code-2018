#!/usr/bin/env python3

with open('input') as f: 
    content = f.readlines()

content = list(map(lambda x: x.strip(), content))

# part 1
from collections import Counter

two_count = 0
three_count = 0
for word in content:
    counter = Counter(list(word))
    two_occurrences = map(lambda x: x[1] == 2, counter.most_common())
    three_occurrences = map(lambda x: x[1] == 3, counter.most_common())
    if any(two_occurrences):
        two_count += 1
    if any(three_occurrences):
        three_count += 1

print(two_count * three_count)

# part 2
