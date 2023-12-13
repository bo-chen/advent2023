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
        ls.append(lstripped)

pats = []
cp = []
for l in ls:
    if l == "":
        pats.append(cp)
        cp = []
        continue
    a = []
    for c in l:
        if c == ".":
            a.append(0)
        else:
            a.append(1)
    cp.append(a)
pats.append(cp)

res = 0
for p in pats:
    h = len(p)
    w = len(p[0])

    reflect = True
    hasfound = False
    # check x
    for x in range(w -1):
        reflect = True
        for j in range(h):
            if not reflect:
                break
            for i in range(w):
                if x - i >= 0 and x + i + 1 < w:
                    if p[j][x - i] != p[j][x + i + 1]:
                        reflect = False
                        break

        if reflect:
            res += x +1 
            hasfound = True
            break
    
    if hasfound:
        continue

    # check y
    for y in range(h -1):
        reflect = True
        for j in range(h):
            if y - j >= 0 and y + j + 1 < h:
                if p[y - j] != p[y + j + 1]:
                    reflect = False
                    break

        if reflect:
            res += 100 * (y + 1)
            break

    if not reflect:
        print("BAD")

print(res)


    

    

    

        

