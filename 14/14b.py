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

mp = []
for l in ls:
    a = []
    for c in l:
        a.append(c)
    mp.append(a)
mp = np.array(mp)

def tiltn(mp):
    for i in range(w):
        obs = -1
        for j in range(h):
            c = mp[j][i]
            if c == "#":
                obs = j
            if c == "O":
                obs += 1
                mp[j][i] = "."
                mp[obs][i] = "O"

cache = {}

def cycle(mp):

    tiltn(mp)
    mp = np.rot90(mp, 3)
    tiltn(mp)
    mp = np.rot90(mp, 3)
    tiltn(mp)
    mp = np.rot90(mp, 3)
    tiltn(mp)
    mp = np.rot90(mp, 3)

    return mp

i = 0
repeated = False
while i < 1000000000:
    if not repeated:
        k = mp.tostring()
        if k in cache:
            lasti = cache[k]
            periods = int((1000000000 - 1 - i) /  (i - lasti))
            i += periods * (i - lasti)
        else:
            cache[k] = i

    mp = cycle(mp)
    i+= 1

res = 0
for i in range(w):
    for j in range(h):
        c = mp[j][i]
        if c == "O":
            res += h - j

print(res)
        
        