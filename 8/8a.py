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

ins = ls[0]

nodes = {}
for l in ls[1:]:
    nodes[l[:3]] = [l[7:10], l[12:15]]

n = "AAA"
i = 0
l = len(ins)
while n != "ZZZ":
    if ins[i % l] == "L":
        n = nodes[n][0]
    else:
        n = nodes[n][1]
    i += 1

print(i)

