import math
import numpy as np
import os
import re
import sys
from functools import reduce
from pathlib import Path

source_path = Path(__file__).resolve()
source_dir = source_path.parent

def pm(m):
    for r in m:
        s = ""
        for c in r:
            print(c, end="")
        print("")

def stoia(pstr):
    return list(map(lambda x: int(x), pstr.split(",")))

def iatos(p):
    return ",".join(map(lambda x: str(x), p))

ls = []
with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

grid = []
for l in ls:
    a = []
    hasgal = False
    for c in l:
        a.append(c)
        if c == "#":
            hasgal = True
    grid.append(a)
    b = []
    if not hasgal:
        for c in l:
            b.append(".")
        grid.append(b)

pm(grid)
addcols = []
for i in range(len(grid[0])):
    hasgal = False
    for l in grid:
        if l[i] == "#":
            hasgal = True
            break
    if not hasgal:
        addcols.append(i)

for ci in reversed(addcols):
    for l in grid:
        l.insert(ci, ".")

w = len(grid[0])
h = len(grid)
stars = []
for j in range(h):
    for i in range(w):
        if grid[j][i] == "#":
            stars.append([i,j])

sumd = 0
for star1 in stars:
    for star2 in stars:
        if star1 != star2:
            sumd += abs(star1[0] - star2[0]) + abs(star1[1]-star2[1])

print(sumd/2)






    




