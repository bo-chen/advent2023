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
with open(f'{source_dir}/s.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

w = len(ls[0])
h = len(ls)
s = (ls[0].find("."),0)
e = (ls[h-1].find("."),h-1)

def longest(s, e):
    cq = [[s, 0]]
    been = set([s])
    maxl = 0
    while cq:
        p, l = cq.pop()
        if p == e:
            print(f"path: {l}")
            if l > maxl:
                maxl = l
            continue
        if l < 0:
            been.remove(p)
            continue
        been.add(p)
        # -1 means backtrack
        cq.append([p, -1])
        nexts = []
        c = ls[p[1]][p[0]]
        if c == ">":
            nexts = [(p[0]+1, p[1])]
        elif c == "^":
            nexts = [(p[0], p[1]-1)]
        elif c == "<":
            nexts = [(p[0]-1, p[1])]
        elif c == "v":
            nexts = [(p[0], p[1]+1)]
        elif c == ".":
            nexts = [(p[0]+1, p[1]), 
                     (p[0], p[1]-1), 
                     (p[0]-1, p[1]),
                     (p[0], p[1]+1)]
        else:
            print("Bad")

        for n in nexts:
            if n in been or n[0] < 0 or n[0] >= w or n[1] < 0 or n[1] >= h:
                continue
            nc = ls[n[1]][n[0]] 
            if nc == "#":
                continue
            cq.append([n,l+1])

    return maxl

print(longest(s, e))

