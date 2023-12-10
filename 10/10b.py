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

s = []
for i, l in enumerate(ls):
    if "S" in l:
        s = [l.index("S"),i]

n = []
dirs = [[1,0],[0,1],[0,-1],[-1,0]]
syms = {"|":[[0,1],[0,-1]],"-":[[1,0],[-1,0]],"L":[[0,-1],[1,0]],
        "J":[[0,-1],[-1,0]],"7":[[-1,0],[0,1]],"F":[[1,0],[0,1]],".":[]}
c = []
pd = []
for d in dirs:
    n = [s[0]+d[0],s[1]+d[1]]
    nsp = ls[n[1]][n[0]]
    nsym = syms[nsp]
    for sd in nsym:
        if sd[0] == -1 * d[0] and sd[1] == -1 * d[1]:
            c = n
            pd = [-1 * d[0], -1 * d[1]]
            spd = pd
            st = c
            break
w = len(ls[0])
h = len(ls)

grid = []
for y in range(h):
    a = []
    for x in range(w):
        a.append(" ")
    grid.append(a)


tiles = set(iatos(s))
def floodi(p):
    # true if touching side
    if p[0] < 0 or p[0] >= w or p[1] < 0 or p[1] >= h:
        return
    if iatos(p) in tiles:
        return
    if grid[p[1]][p[0]] == "i":
        return
    if ls[p[1]][p[0]] == "S":
        return

    grid[p[1]][p[0]] = "i"
    for d in dirs:
        floodi([p[0] + d[0], p[1] + d[1]])

    return

# pd, LR?, R tile
handm = {"|":[[0,1],"",[[1,0]], [[-1,0]]],
        "-":[[1,0],"",[[0,-1]], [[0,1]]],
        "L":[[0,-1],"L",[[-1,1],[-1,0],[0,1]], [[1,-1]]],
        "J":[[0,-1],"R",[[-1,-1]],[[1,1],[0,1],[1,0]]],
        "7":[[-1,0],"R",[[-1,1]],[[1,-1],[1,0],[0,-1]]],
        "F":[[1,0],"L",[[-1,-1],[-1,0],[0,-1]],[[1,1]]]}

steps = 0
# pos for right
turns = 0
while c[0] != s[0] or c[1] != s[1]:
    tiles.add(iatos(c))
    csym = syms[ls[c[1]][c[0]]]
    for sd in csym:
        if sd[0] == pd[0] and sd[1] == pd[1]:
            hand = handm[ls[c[1]][c[0]]]
            if hand[0][0] == pd[0] and hand[0][1] == pd[1]:
                if hand[1] == "R":
                    turns += 1
                if hand[1] == "L":
                    turns -= 1
            else:
                # opposite
                if hand[1] == "R":
                    turns -= 1
                if hand[1] == "L":
                    turns += 1
        else:
            nc = [c[0]+sd[0],c[1]+sd[1]]
            npd = [-1 * sd[0], -1 * sd[1]]
    c = nc
    pd = npd
    steps += 1

paintside = 0
if turns > 0:
    paintside = 1
elif turns < 0:
    paintside = -1
else:
    raise "no turns?"

# now paint
c = st
pd = spd
while c[0] != s[0] or c[1] != s[1]:
    csym = syms[ls[c[1]][c[0]]]
    for sd in csym:
        if sd[0] == pd[0] and sd[1] == pd[1]:
            hand = handm[ls[c[1]][c[0]]]
            paints = []
            rightway = hand[0][0] == pd[0] and hand[0][1] == pd[1]
            if rightway and paintside == 1 or not rightway and paintside == -1:
                paints = hand[2]
            else:
                paints = hand[3]
            for paintd in paints:
                floodi([c[0] +paintd[0], c[1] + paintd[1]])
        else:
            nc = [c[0]+sd[0],c[1]+sd[1]]
            npd = [-1 * sd[0], -1 * sd[1]]
    c = nc
    pd = npd

enc = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "i":
            enc += 1

pm(grid)
print(enc)




