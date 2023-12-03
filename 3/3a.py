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

def ispartstr(s):
    if s == ".":
        return False
    if s.isalnum():
        return False
    return True

sum = 0
w = len(ls[0])
h = len(ls)
linei = 0
for l in ls:
    if l == "":
        continue

    ms = re.finditer("\d+",l)
    for m in ms:
        ispart = False
        if m.start() > 0:
            for j in [-1, 0, 1]:
                testlinei = linei + j
                if testlinei >=0 and testlinei < h:
                    if ispartstr(ls[testlinei][m.start() - 1]):
                        ispart = True
                        break
                if ispart:
                    break
        
        if m.end() < w:
            for j in [-1, 0, 1]:
                testlinei = linei + j
                if testlinei >=0 and testlinei < h:
                    if ispartstr(ls[testlinei][m.end()]):
                        ispart = True
                        break
                if ispart:
                    break
        
        for i in range(m.start(), m.end()):
            for j in [-1, 0, 1]:
                testlinei = linei + j
                if testlinei >=0 and testlinei < h:
                    if ispartstr(ls[testlinei][i]):
                        ispart = True
                        break
                if ispart:
                    break
            if ispart:
                break

        if ispart:
            sum += int(m[0])

    linei += 1

print(sum)

