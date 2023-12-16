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

w = len(ls[0])
h = len(ls)

def newDir(bdir, pos):
    c = ls[pos[1]][pos[0]]
    dirmap = {"\\": {(1,0) : [(0,1)], (0,-1): [(-1,0)], 
                     (-1,0) : [(0,-1)], (0,1): [(1,0)]},
              "/": {(1,0) : [(0, -1)], (0,-1): [(1,0)], 
                     (-1,0): [(0,1)], (0,1): [(-1,0)]},
                "-": {(1,0) : [(1, 0)], (0,-1): [(-1,0), (1,0)], 
                     (-1,0): [(-1,0)], (0,1): [(-1,0), (1, 0)]},
                "|": {(1,0) : [(0,-1), (0,1)], (0,-1): [(0,-1)], 
                     (-1,0): [(0,-1),(0,1)], (0,1): [(0,1)]}} 
    if c == ".":
        return [bdir]
    else: 
        return dirmap[c][bdir]


def testE(sd, sp):
    m = []
    for l in ls:
        a = []
        for c in l:
            a.append(set())
        m.append(a)

    bdirs = [sd]
    ps = [sp]

    while len(ps) != 0:
        nbdirs = []
        nps = []
        for i in range(len(ps)):
            p = ps[i]
            d = bdirs[i]
            m[p[1]][p[0]].add(d)
            ndres = newDir(d, p)
            for nbd in ndres:
                np = (p[0] + nbd[0], p[1] + nbd[1])
                if np[0] < 0 or np[0] >= w or np[1] < 0 or np[1] >= h:
                    continue
                if nbd in m[np[1]][np[0]]:
                    continue
                nbdirs.append(nbd)
                nps.append(np)
        bdirs = nbdirs
        ps = nps

    res = 0
    for a in m:
        for s in a:
            if len(s) > 0: 
                res += 1
    return res

mx = 0
for j in range(h):
    r = testE((1,0), (0, j))
    if r > mx:
        mx = r
    r = testE((-1,0), (w -1, j))
    if r > mx:
        mx = r


for i in range(w):
    r = testE((0,1), (i, 0))
    if r > mx:
        mx = r
    r = testE((0,-1), (i, h-1))
    if r > mx:
        mx = r

print(mx)

