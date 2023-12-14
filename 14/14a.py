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

res = 0
for i in range(w):
    obs = -1
    for j in range(h):
        c = ls[j][i]
        if c == "#":
            obs = j
        if c == "O":
            load = h - (obs + 1)
            res += load
            obs += 1

print(res)
        
        