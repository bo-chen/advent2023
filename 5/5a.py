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
        ls.append(lstripped)

def readns(st):
    return list(map(lambda x: int(x), st.split(" ")))

def readmap(i):
    m = []
    while i < len(ls) and ls[i] != "":
        m.append(readns(ls[i]))
        i += 1

    i += 2
    return [i, m]

ss = readns(ls[0][7:])
i = 3

i, setso = readmap(i)
i, sotf = readmap(i)
i, ftw = readmap(i)
i, wtli = readmap(i)
i, litt = readmap(i)
i, tth = readmap(i)
i, htolo = readmap(i)

def mapone(m, n):
    for dest, src, l in m:
        if n >= src and n < src + l:
            return n - src + dest
        
    return n


mi = 238571923579180253
for s in ss:
    t = mapone(setso, s)
    t = mapone(sotf, t)
    t = mapone(ftw, t)
    t = mapone(wtli, t)
    t = mapone(litt, t)
    t = mapone(tth, t)
    t = mapone(htolo, t)

    if t < mi:
        mi = t

print(mi)
