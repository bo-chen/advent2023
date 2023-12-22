import math
import numpy as np
import os
import re
import sys
import copy
import operator
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

bricks = []
for l in ls:
    v1str, v2str = l.split("~")
    s = np.array(stoia(v1str))
    e = np.array(stoia(v2str))
    if s[2] > e[2]:
        bricks.append([e, s])
    else:
        bricks.append([s, e])

def bhcmp(b1, b2):
    if b1[0][2] < b2[0][2]:
        return -1
    if b1[0][2] > b2[0][2]:
        return 1
    return 0

bricks.sort(key=cmp_to_key(bhcmp))

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

hbyxy = {}
bricksupports = {}
bricksupportedby = {}
for i, b in enumerate(bricks):
    minfh = 10000000000
    minbrickis = set()
    s, e = b

    v = e - s
    norm = np.linalg.norm(v)
    dir = v
    if norm != 0:
        dir = v / norm
    # don't check other blocks if the block is up down
    for j in range(int(norm) + 1):
        p = s + j * dir
        xy = (p[0], p[1])
        if xy in hbyxy:
            h, bi = hbyxy[xy]
            fh = p[2] - h - 1
            if fh == minfh:
                minbrickis.add(bi)
            elif fh < minfh:
                minfh = fh
                minbrickis = set([bi])
            if fh < 0:
                print("negative?")
    if len(minbrickis) == 0:
        minfh = s[2] - 1

    # set max heights
    for j in range(int(norm + 1)):
        p = s + j * dir
        xy = (p[0], p[1])
        nh = p[2] - minfh
        if xy in hbyxy and hbyxy[xy][0] >= nh:
            print("bad")

        hbyxy[xy] = [p[2] - minfh, i]

    # bricksupports
    bricksupportedby[i] = minbrickis
    for mbi in minbrickis:
        if mbi in bricksupports:
            bricksupports[mbi].append(i)
        else:
            bricksupports[mbi] = [i]

safebricks = 0
for i, b in enumerate(bricks):
    if i in bricksupports:
        allbricksdoublesupported = True
        for j in bricksupports[i]:
            if len(bricksupportedby[j]) < 2:
                allbricksdoublesupported = False
        if allbricksdoublesupported:
            safebricks +=1
    else:
        safebricks += 1

print(safebricks)


            



