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

maxes = {"r": 12, "g": 13, "b": 14}
count = 0

for l in ls:
    if l == "":
        continue

    result = re.search("Game (\d+):(.*)$", l)
    id = int(result[1])

    cool = True
    cubes = re.split(";|,", result[2])
    for c in cubes:
        rs = re.search("(\d+) (\w)", c)
        if int(rs[1]) > maxes[rs[2]]:
            cool = False
            break

    if cool:
        count = count + id

print(count)


            
