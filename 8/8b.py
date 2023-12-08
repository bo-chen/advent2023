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

st = 0
cns = []
for n in nodes.keys():
    if n[2] == "A":
        cns.append(n)
scns = cns.copy()

def isend(cns):
    for n in cns:
        if n[2] != "Z":
            return False
        
    return True

print(cns)
zdone = []
zphases = []
for _ in cns:
    zphases.append({})
    zdone.append(False)

# Actual cycles
[{'GLZ': [18113, 36226]}, 
 {'MFZ': [22411, 44822]}, 
 {'JPZ': [21797, 43594]}, 
 {'VSZ': [14429, 28858]}, 
 {'ZZZ': [16271, 32542]}, 
 {'BJZ': [18727, 37454]}]

# actual answer after factorization
print(59*73*71*47*53*61*307)

i = 0
l = len(ins)
while not isend(cns):
    for j in range(len(cns)):
    # find cycle time and remainder
        n = cns[j]
        if n[2] == "Z" and not zdone[j]:
            if n in zphases[j]:
                zphases[j][n].append(i)
                zdone[j] = True
                print(zphases)
                if all(zdone):
                    print("all cycles done")
                    for d in zphases:
                        for k in d:
                            print(k)
                            print(d[k])
                            print(d[k][1] - d[k][0])
            else:
                zphases[j][n] = [i]

        if ins[i % l] == "L":
            cns[j] = nodes[n][0]
        else:
            cns[j] = nodes[n][1]
    i += 1

print(i)

