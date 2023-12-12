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

def valid(spv, assigned):
    if len(spv) != len(assigned):
        return False
    for i, c in enumerate(assigned):
        if c != spv[i] and spv[i] != "?":
            return False
    return True

def validperms(spvleft, gsleft, lleft):
    if lleft < 0 or sum(gsleft) + len(gsleft) - 1 > lleft:
        return 0

    if len(gsleft) == 1:
        res = 0
        for n in range(lleft - gsleft[0] + 1):
            if valid(spvleft, ["."] * n + ["#"] * gsleft[0] + ["."] * (lleft - n - gsleft[0])):
                res += 1
        return res

    res = 0
    for n in range(lleft -  (sum(gsleft) + len(gsleft) - 1) + 1):
        used = n + gsleft[0] + 1
        if valid(spvleft[:used], ["."] * n + ["#"] * gsleft[0] + ["."]):
            res += validperms(spvleft[used:], gsleft[1:], lleft - used)

    return res

final = 0
for i, l in enumerate(ls):
    [spv, gsstr] = l.split(" ")
    gs = list(map(lambda x: int(x), gsstr.split(",")))
    res = validperms(spv, gs, len(spv))
    print(str(i) + " " + str(res))
    final += res

print(final)


    
