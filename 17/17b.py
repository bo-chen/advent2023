import math
import numpy as np
import os
import re
import sys
import copy
import heapq as hq
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

w = len(ls[0])
h = len(ls)
p = (0,0)
fmoves = 0
dir = (1,0)

been = set()
boundary = []
# (heat, pos, dir, numforward, paths)
hq.heappush(boundary, (0,(0,0),(0,0),0,[]))

while len(boundary) != 0:
    b = hq.heappop(boundary)
    heat = b[0]
    lp = b[1]
    ld = b[2]
    fors = b[3]
    if lp[0] == w-1 and lp[1] == h-1 and fors >= 4:
        print(heat)
        break
    for d in ((1,0), (-1,0), (0,1), (0,-1)):
        if d[0] == -1 * ld[0] and d[1] == -1 * ld[1]:
            continue
        if fors >= 10 and d == ld:
            continue
        if fors < 4 and d != ld and lp != (0,0):
            continue
        npos = (lp[0] + d[0], lp[1] + d[1]) 
        if npos[0] < 0 or npos[0] >= w or npos[1] < 0 or npos[1] >= h:
            continue
        nfor = 1
        if d == ld:
            nfor = fors + 1
        if (npos, d, nfor) in been:
            continue
        been.add((npos, d, nfor))
        newp = b[4].copy()
        newp.append(npos)
        hq.heappush(boundary, (heat + int(ls[npos[1]][npos[0]]), 
                               npos, d, nfor, newp))



    

