import math
import numpy as np
import os
import re
import sys
import copy
from functools import *
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

w = 2000
h = 2000

map = []
for j in range(h):
    a = []
    for i in range(w):
        a.append((" ",[]))
    map.append(a)

p = (int(w/2), int(h / 2))
startp = p
# (color, [pipedirs])
map[p[1]][p[0]] = ("0",[(0,0)])

dirv = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}
miny = 1547295  
maxy = -1
for i, l in enumerate(ls):
    m  = re.search("^(\w) (\d+) ..(.+).$", l)
    d = dirv[m[1]]
    dist = int(m[2])
    color = m[3]
    map[p[1]][p[0]][1].append(d)

    for step in range(dist):
        x = p[0] + d[0]
        y = p[1] + d[1]
        p = (x, y)
        if y > maxy:
            maxy = y
        if y < miny:
            miny = y
        map[y][x] = (color, map[y][x][1] + [d])
        #map[p[1]][p[0]] = "@"

res = 0
pipedir = (0,0)
for j in range(miny, maxy + 1):
    isin = False
    for i in range(w):
        c, ds = map[j][i]
        if c != " ":
            for d in ds:  
                if d == (0,1) or d == (0,-1):
                    if pipedir == (0,0):
                        pipedir = d
                    elif pipedir != d:
                        isin = not isin
            res += 1
        if pipedir != (0,0) and c == " ":
            isin = not isin
            pipedir = (0,0)
        if c == " " and isin:
            map[j][i] = "1"
            res += 1
#pm(map)
print(res)
