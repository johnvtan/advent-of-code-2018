#!/usr/bin/env python3

with open('input') as f:
    content = f.readlines()

def get_coords(line):
    coords = list(map(lambda x: x.strip(), line.split(',')))
    return int(coords[0]), int(coords[1])

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

coords = [(get_coords(line)) for line in content]

min_x = min(coords, key=lambda x: x[1])[1]
max_x = max(coords, key=lambda x: x[1])[1]

min_y = min(coords, key=lambda x: x[0])[0]
max_y = max(coords, key=lambda x: x[0])[0]

area = [0 for i in range(len(coords))]
infinite_ids = set() 
area_under_10000 = 0
for x in range(min_x-1, max_x+1):
    for y in range(min_y-1, max_y+1):
        point = (x, y)
        # find distances to each coordinate
        distances = list(map(lambda c: manhattan_distance(c, point), coords))
        if sum(distances) < 10000:
            area_under_10000 += 1
        min_dist = min(distances)
        if distances.count(min_dist) == 1:
            index = distances.index(min_dist)
            area[index] += 1
            if x == min_x or x == max_x or y == min_y or y == max_y:
                infinite_ids.add(index)
        
# remove all the points with infinite area
no_inf = [area[i] for i in range(len(area)) if i not in infinite_ids]
print(max(no_inf))

print(area_under_10000)
