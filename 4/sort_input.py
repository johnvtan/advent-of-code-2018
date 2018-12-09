#!/usr/bin/env python3

with open('input') as f:
    content = f.readlines()

sorted_content = sorted(content, key=lambda x: x[1:17])

with open('sorted-input', 'w+') as f:
    f.writelines(sorted_content) 
