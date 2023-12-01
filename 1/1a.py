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

sum = 0
for l in ls:
    if l == "":
        continue
    f = re.search("\d", l)
    print(l)
    print(f)
    s = re.search("\d", l[::-1])
    print(l[::-1])
    print(s)
    sum = sum + int(f[0]+s[0])


print(sum)