#!/usr/bin/env python3

with open('input') as f: 
    content = map(lambda x: x.strip(), f.readlines())

class Claim:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def print_claim(self):
        print("Claim: (%d, %d)->(%d, %d)" % (self.x, self.y, self.x+self.width, self.y+self.width))

class Fabric:
    def __init__(self, width=1000, height=1000):
        self.state = [[0 for i in range(height)] for j in range(width)]

    def update(self, claim):
        for i in range(claim.width):
            for j in range(claim.height):
                self.state[claim.x + i][claim.y + j] += 1

    def overlap(self):
        count = 0
        for row in self.state:
            count += len(list(filter(lambda x: x > 1, row)))
        return count

    def print_state(self):
        for row in self.state:
            print(row)

def parse_input(line):
    coords = line.split('@')[1]    
    xy, width_height = coords.split(':')
    x, y = xy.split(',')
    width, height = width_height.split('x')
    return Claim(int(x.strip()), int(y.strip()), int(width.strip()), int(height.strip()))

claims = []
for line in content:
    claims.append(parse_input(line))

print(len(claims))
fabric = Fabric()
for claim in claims:
    fabric.update(claim)

print(fabric.overlap())
