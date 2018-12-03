#!/usr/bin/env python3

with open('input') as f: 
    content = map(lambda x: x.strip(), f.readlines())

class Claim:
    def __init__(self, x, y, width, height):
        self.top_left = (x, y)
        self.top_right= (x + width, y + height)

class Fabric:
    def __init__(self, width=1000, height=1000):
        self.state = ((0,) * width * height)

    def update(self, claim):
        

    def get_index(self, x, y):
        return x*y

    def overlap(self):
        pass

def parse_input(line):
    coords = line.split('@')[1]    
    xy, width_height = coords.split(':')
    x, y = xy.split(',')
    width, height = width_height.split('x')
    print('({0}, {1}) -> ({2}, {3})'.format(x, y, width, height))
    return Claim(int(x.strip()), int(y.strip()), int(width.strip()), int(height.strip()))

claims = []
for line in content:
    claims.append(parse_input(line))

fabric = Fabric()
for claim in claims:
    fabric.update(claim)

print(fabric.overlap())
