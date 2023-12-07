import math
import numpy as np
import os
import re
import sys
from functools import reduce
import functools
from pathlib import Path
from collections import Counter

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


def convert_to_num(hand):
    res = []
    for c in hand:
        cm = {"T":10, "J": 11, "Q": 12, "K": 13, "A": 14}
        if c in cm:
            res.append(cm[c])
        else:
            res.append(int(c))
    return res

def typenum(h):
    freqs = sorted(Counter(h).values(), reverse=True)

    if freqs[0] == 5:
        return 7
    if freqs[0] == 4:
        return 6
    if freqs[0:2] == [3,2]:
        return 5
    if freqs[0] == 3:
        return 4
    if freqs[0:2] == [2,2]:
        return 3
    if freqs[0] == 2:
        return 2
    return 1
    
hps = []
for l in ls:
    hps.append([typenum(l[:5]), convert_to_num(l[:5]), l[:5], int(l[6:])])

hpss = sorted(hps)

sum = 0
for i, hp in enumerate(hpss):
    sum += (i+1) * hp[3]

print(sum)
