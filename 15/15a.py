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


res = 0
def hashy(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    
    return h

a = []
for l in ls:
    for c in l:
        if c == ",":
            res += hashy(a)
            a = []
        else:
            a.append(c)

res += hashy(a)
print(res)


