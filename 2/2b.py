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

count = 0

for l in ls:
    if l == "":
        continue

    maxes = {"r": 0, "g": 0, "b": 0}

    result = re.search("Game (\d+):(.*)$", l)
    id = int(result[1])

    cubes = re.split("[;,]", result[2])
    for c in cubes:
        rs = re.search("(\d+) (\w)", c)
        n = int(rs[1])
        if n > maxes[rs[2]]:
            maxes[rs[2]] = n

    count += maxes["r"] * maxes["b"] * maxes["g"]

print(count)


            
