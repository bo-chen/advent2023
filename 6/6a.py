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

times = list(map(lambda x: int(x), re.split("\s+", ls[0][6:].strip())))
dists = list(map(lambda x: int(x), re.split("\s+", ls[1][11:].strip())))

prod = 1

for i in range(len(times)):
    t = times[i]
    d = dists[i]

    n = 0
    for h in range(t):
        if d < h * (t - h):
            n += 1

    prod *= n

print(prod)
