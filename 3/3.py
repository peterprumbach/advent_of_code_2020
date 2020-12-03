import numpy as np
map = []

#Open map file
with open('3/map') as file:
    map = file.readlines()

count = 0
position = 0

for i in range(0, len(map), 1):
    row = map[i][:-1]
    if('#' == row[position%len(row)]):
        count+=1
    position += 3

print("part1: ", count)