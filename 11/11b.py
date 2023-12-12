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
addlines = []
for i, l in enumerate(ls):
    a = []
    hasgal = False
    for c in l:
        a.append(c)
        if c == "#":
            hasgal = True
    grid.append(a)
    if not hasgal:
        addlines.append(i)

addcols = []
for i in range(len(grid[0])):
    hasgal = False
    for l in grid:
        if l[i] == "#":
            hasgal = True
            break
    if not hasgal:
        addcols.append(i)

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
            ad = 0
            for li in addlines:
                if star1[1] < li and li < star2[1] or star1[1] > li and li > star2[1]:
                    ad += 1000000 - 1
            for ci in addcols:
                if star1[0] < ci and ci < star2[0] or star1[0] > ci and ci > star2[0]:
                    ad += 1000000 - 1
            sumd += abs(star1[0] - star2[0]) + abs(star1[1]-star2[1]) + ad

print(sumd/2)






    




