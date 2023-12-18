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

p = (0,0)
startp = p

dirv = {"3": (0,-1), "2": (-1,0), "1": (0,1), "0": (1,0)}
miny = 1547295  
maxy = -1
det = 0
distt = 0
for i, l in enumerate(ls):
    m  = re.search("^(\w) (\d+) ..(.....)(.).$", l)
    d = dirv[m[4]]
    dist = int(m[3], 16)
    distt += dist

    x = p[0] + d[0] * dist
    y = p[1] + d[1] * dist
    det += x * p[1] - y * p[0]
    p = (x, y)
        
print(distt / 2 + abs(det)/ 2 + 1)
