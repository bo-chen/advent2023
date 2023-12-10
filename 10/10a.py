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
syms = {"|":[[0,1],[0,-1]],"-":[[1,0],[-1,0]],"L":[[0,-1],[1,0]],"J":[[0,-1],[-1,0]],"7":[[-1,0],[0,1]],"F":[[1,0],[0,1]],".":[]}
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
            break

steps = 0
while c[0] != s[0] or c[1] != s[1]:
    csym = syms[ls[c[1]][c[0]]]
    for sd in csym:
        if sd[0] == pd[0] and sd[1] == pd[1]:
            continue
        c = [c[0]+sd[0],c[1]+sd[1]]
        pd = [-1 * sd[0], -1 * sd[1]]
        break
    steps += 1

print(math.ceil(steps / 2))

    








