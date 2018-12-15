#!/usr/bin/env python3

with open('input') as f:
    content = f.readlines()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Instruction:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.completed = False
        self.in_progress = False
        self.time_left = 60 + alphabet.index(name) + 1
    
    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def can_complete(self):
        return all([p.completed for p in self.parents]) or len(self.parents) == 0

    def print_relatives(self):
        print("Instruction {0}: ".format(self.name))
        print("\tParents: ", [i.name for i in self.parents])
        print("\tChildren: ", [i.name for i in self.children])

instructions = [Instruction(c) for c in alphabet]
for line in content:
    parent = instructions[alphabet.index(line[5])]
    child = instructions[alphabet.index(line[36])]
    parent.add_child(child)
    child.add_parent(parent)

# remove all instructions with no parents or children
filtered = list(filter(lambda x: len(x.children) > 0 or len(x.parents) > 0, instructions))
to_complete = list(filter(lambda x: len(x.parents) == 0, filtered))
order = []
while len(to_complete) > 0:
    to_complete = sorted(to_complete, key=lambda x: x.name)
    curr = to_complete.pop(0)
    curr.completed = True
    order.append(curr.name)
    to_complete += [c for c in curr.children if c.can_complete()]

for i in filtered:
    i.print_relatives()

print(''.join(order))

NUM_WORKERS = 5
def schedule(to_complete):
    assert len([i for i in to_complete if i.in_progress]) < NUM_WORKERS+1
    for ins in to_complete:
        if len(list(filter(lambda x: x.in_progress == True, to_complete))) >= NUM_WORKERS:
            print('too many')
            break
        if all([i.in_progress for i in to_complete]):
            break
        ins.in_progress = True    

def remove_completed(to_complete):
    for i, ins in reversed(list(enumerate(list(to_complete)))):
        if ins.in_progress == True and ins.time_left == 0:
            ins.in_progress == False
            ins.completed = True
            to_complete.pop(i)
            new = [c for c in ins.children if c.can_complete()]
            already_in_progress = [i.name for i in to_complete]
            for c in new:
                if c.name not in already_in_progress:
                    to_complete.append(c)

def tick(to_complete):
    for ins in to_complete:
        if ins.in_progress and ins.time_left > 0:
            ins.time_left -= 1

instructions = [Instruction(c) for c in alphabet]
for line in content:
    parent = instructions[alphabet.index(line[5])]
    child = instructions[alphabet.index(line[36])]
    parent.add_child(child)
    child.add_parent(parent)

filtered = list(filter(lambda x: len(x.children) > 0 or len(x.parents) > 0, instructions))
to_complete = list(filter(lambda x: len(x.parents) == 0, filtered))
done = False
time = 0
while len(to_complete) > 0:
    to_complete = sorted(to_complete, key=lambda x: x.name)
    tick(to_complete)
    remove_completed(to_complete)
    schedule(to_complete)
    time += 1

# not sure why i was off by one?
print(time-1)
