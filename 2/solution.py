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
def match(w1, w2):    
    matching = [x == y for (x, y) in zip(list(w1), list(w2))] 
    if matching.count(False) == 1:
        return ''.join([w1[i] for i in range(len(matching)) if matching[i]])
    return False

assert match("abcd", "abce") == "abc" 
assert match("dace", "dbce") == "dce"
assert match("abcd", "abcd") == False
assert match("abcd", "bcda") == False

for index, word in enumerate(content):
    for second_word in content[index:]:
        rv = match(word, second_word)
        if not rv:
            continue
        print(rv)

