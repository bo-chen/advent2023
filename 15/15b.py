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


def hashy(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    
    return h

boxes = []
for i in range(256):
    boxes.append([])

a = []
for l in ls:
    ops = l.split(",")
    for op in ops:
        m = re.search("^(\w+)([=-])(\d*)$", op)
        label = m[1]
        bi = hashy(label)
        if m[2] == "-":
            ri = -1
            for j in range(len(boxes[bi])):
                if boxes[bi][j][0] == label:
                    ri = j
                    break
            if ri >= 0:
                del boxes[bi][j]
        elif m[2] == "=":
            ri = -1
            for j in range(len(boxes[bi])):
                if boxes[bi][j][0] == label:
                    ri = j
                    break
            if ri >= 0:
                boxes[bi][ri] = [label, m[3]]
            else:
                    boxes[bi].append([label, m[3]])

res = 0
for i, b in enumerate(boxes):
    for j, lens in enumerate(b):
        res += (i + 1) * (j + 1) * int(lens[1])

print(res)


