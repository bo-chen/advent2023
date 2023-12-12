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

cache = {}

def validperms(spvleft, gsleft):
    lleft = len(spvleft)
    if sum(gsleft) + len(gsleft) - 1 > lleft:
        return 0
    if gsleft == []:
        if spvleft.find("#") != -1:
            return 0
        else:
            return 1
    
    key = spvleft + iatos(gsleft)
    if key in cache:
        return cache[key]
    
    if len(gsleft) == 1:
        res = 0
        for n in range(lleft - gsleft[0] + 1):
            if valid(spvleft, ["."] * n + ["#"] * gsleft[0] + ["."] * (lleft - n - gsleft[0])):
                res += 1
        cache[key] = res
        return res

    res = 0
    for n in range(lleft -  (sum(gsleft) + len(gsleft) - 1) + 1):
        used = n + gsleft[0] + 1
        if valid(spvleft[:used], ["."] * n + ["#"] * gsleft[0] + ["."]):
            res += validperms(spvleft[used:], gsleft[1:])

    cache[key] = res
    return res

def checkgroups(spvs, gsleft):
    if len(spvs) == 1:
        return validperms(spvs[0], gsleft)
    if spv[0] == "":
        return checkgroups(spvs[1:], gsleft)

    key = ".".join(spvs) + iatos(gsleft)
    if key in cache:
        return cache[key]
    
    res = 0
    for n in range(len(gsleft) + 1):
        ps = 1
        ps = validperms(spvs[0], gsleft[:n])
        psrest = 0
        if ps > 0:
            psrest = checkgroups(spvs[1:], gsleft[n:])
        res += psrest * ps

    cache[key] = res
    return res


final = 0
for i, l in enumerate(ls):
#i = 11
#l = ls[i]
#for l in [l]:
    [spv, gsstr] = l.split(" ")
    spv = (spv + "?") * 4 + spv
    gsstr = (gsstr + ",") * 4 + gsstr
    gs = list(map(lambda x: int(x), gsstr.split(",")))
    res = checkgroups(spv.split("."), gs)
    print(str(i) + " " + str(res))
    final += res

print(final)


    
