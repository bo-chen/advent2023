import math
import numpy as np
import os
import re
import sys
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
        l = line.strip()
        ls.append(l)

h = len(ls)
copies = [1] * h

for i, l in enumerate(ls):
    if l == "":
        continue

    linem = re.search("^([^:]+):([^|]+)\|(.+)$", l)
    
    wins = set()
    for w in re.finditer("\d+", linem[2]):
        wins.add(int(w[0]))

    ms = 0   
    for n in re.finditer("\d+", linem[3]):
        if int(n[0]) in wins:
            ms += 1

    if ms > 0:
        for j in range(i+1, i+1+ms):
            if j < h:
                copies[j] += copies[i]

s = sum(copies)
print(s)