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

    f = re.search("\d|one|two|three|four|five|six|seven|eight|nine", l)
    if f[0] == "one":
        f = "1"
    elif f[0] == "two":
        f = "2"
    elif f[0] == "three":
        f = "3"
    elif f[0] == "four":
        f = "4"
    elif f[0] == "five":
        f = "5"
    elif f[0] == "six":
        f = "6"
    elif f[0] == "seven":
        f = "7"
    elif f[0] == "eight":
        f = "8"
    elif f[0] == "nine":
        f = "9"
    else:
        f = f[0]
    
    s = re.search("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", l[::-1])
    if s[0] == "eno":
        s = "1"
    elif s[0] == "owt":
        s = "2"
    elif s[0] == "eerht":
        s = "3"
    elif s[0] == "ruof":
        s = "4"
    elif s[0] == "evif":
        s = "5"
    elif s[0] == "xis":
        s = "6"
    elif s[0] == "neves":
        s = "7"
    elif s[0] == "thgie":
        s = "8"
    elif s[0] == "enin":
        s = "9"
    else:
        s = s[0]
    sum = sum + int(f+s)


print(sum)