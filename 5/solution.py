#!/usr/bin/env python3

with open('input') as f:
    content = list(f.read().strip())

def react(polymer):
    done = False
    i = 0
    while not done:
        if i + 1 >= len(polymer):
            done = True
        elif polymer[i] != polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
            del polymer[i:i+2]
            if i > 0:
                i -= 1
        else:
            i += 1
    return len(polymer)

print(react(content))

# part 2

polymer_types = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

shortest = len(content)
for p in polymer_types:
    removed_polymer = list(filter(lambda x: x != p and x != p.lower(), content))
    length = react(removed_polymer)
    if length < shortest:
        shortest = length

print(shortest)
