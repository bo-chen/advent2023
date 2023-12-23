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
s = (ls[0].find("."),0)
e = (ls[h-1].find("."),h-1)
shortcuts = {}

def addshortcut(s, spp, e, been, pn):
    p = s
    pp = spp
    l = 0
    while True:
        if p == e:
            break
        nexts = [(p[0]+1, p[1]), 
            (p[0], p[1]-1), 
            (p[0]-1, p[1]),
            (p[0], p[1]+1)]
        ncq = []
        for n in nexts:
            if n[0] < 0 or n[0] >= w or n[1] < 0 or n[1] >= h or (n[0] == pp[0] and n[1] == pp[1]):
                continue
            nc = ls[n[1]][n[0]] 
            if nc == "#":
                continue
            ncq.append(n)
        if len(ncq) == 0:
            shortcuts[s] = [None,None,None]
            return
        if len(ncq) > 1:
            break
        been.add(p)
        pp = p
        p = ncq[0]
        l += 1

    if (pp != spp):
        been.remove(pp)
    shortcuts[pp] = [spp, l, s]
    shortcuts[s] = [p, l, pp]

def longest(s, e):
    cq = [[s, 0, (-1, -1)]]
    been = set([s])
    maxl = 0
    while cq:
        p, l, pp = cq.pop()
        if p == e:
            if l > maxl:
                maxl = l
            continue
        if l < 0:
            been.remove(p)
            continue

        been.add(p)
        # -1 means backtrack
        cq.append([p, -1, None])
        if p in shortcuts:
            np, sl, spp = shortcuts[p]
            if np is None:
                continue
            if np in been:
                continue
            cq.append([np, l + sl, spp])
            continue
        nexts = [(p[0]+1, p[1]), 
                (p[0], p[1]-1), 
                (p[0]-1, p[1]),
                (p[0], p[1]+1)]

        ncq = []
        for n in nexts:
            if n[0] < 0 or n[0] >= w or n[1] < 0 or n[1] >= h or (n[0] == pp[0] and n[1] == pp[1]):
                continue
            nc = ls[n[1]][n[0]] 
            if nc == "#":
                continue
            ncq.append(n)
        
        if len(ncq) == 1:
            addshortcut(p, pp, e, been, ncq[0])
            # redo point
            been.remove(p)
            cq.pop()
            cq.append([p, l, pp])
        else:
            for n in ncq:
                if n not in been:
                    cq.append([n, l+1, p])


    return maxl

print(longest(s, e))

