import numpy as np
map = []

#right, down
step=[3,1]

#Open map file
with open('3/map') as file:
    map = list(file.read().splitlines())

#Expand map

