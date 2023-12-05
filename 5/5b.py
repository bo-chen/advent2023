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

# returns list of ranges
def maprange(m, beg, le):
    for dest, src, l in m:
        if beg >= src and beg + le < src + l:
            return [[beg - src + dest, le]]
        
        if beg >= src and beg < src + l and beg + le >= src + l:
            inn = (src + l) - beg
            return [[beg - src + dest, inn]] + maprange(m, src + l, le - inn)
        
        if beg < src and beg + le > src and beg + le < src + l:
            inn = beg + le - src
            return maprange(m, beg, le - inn) + [[dest, inn]]
        
        if beg < src and beg + le >= src + l:
            outbefore = src - beg
            outafter = beg + le - (src + l)
            return maprange(m, beg, outbefore) + [[dest, l]] + maprange(m, src + l, outafter)
 
    return [[beg, le]]

def mapranges(m, rs):
    res = []
    for r in rs:
        res = res + maprange(m, r[0], r[1])

    return res

mi = 238571923579180253
i = 0
while i < len(ss):
    t = maprange(setso, ss[i], ss[i+1])
    t = mapranges(sotf, t)
    t = mapranges(ftw, t)
    t = mapranges(wtli, t)
    t = mapranges(litt, t)
    t = mapranges(tth, t)
    t = mapranges(htolo, t)

    for p in t:
        if p[0] < mi:
            mi = p[0]
    
    i += 2

print(mi)
