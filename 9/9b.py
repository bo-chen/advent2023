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

res = 0
for l in ls:
    ns = list(map(lambda x: int(x),l.split(" ")))
    diffs = [ns]
    while diffs[-1][0] != 0 or len(set(diffs[-1])) != 1:
        a = []
        for i in range(len(diffs[-1]) - 1):
            a.append(diffs[-1][i+1] - diffs[-1][i])
        diffs.append(a)

    for i in range(len(diffs) - 2, -1, -1):
        diffs[i] = [diffs[i][0] - diffs[i+1][0]] + diffs[i]

    res += diffs[0][0]

print(res)
    



