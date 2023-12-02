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

def wordtoi(word):
    if word == "one":
        return 1
    elif word == "two":
        return 2
    elif word == "three":
        return 3
    elif word == "four":
        return 4
    elif word == "five":
        return 5
    elif word == "six":
        return 6
    elif word == "seven":
        return 7
    elif word == "eight":
        return 8
    elif word == "nine":
        return 9
    else:
        return int(word)


sum = 0
for l in ls:
    if l == "":
        continue

    ms = re.search("(\d|one|two|three|four|five|six|seven|eight|nine).*(\d|one|two|three|four|five|six|seven|eight|nine)", l)
    if ms:
        f = wordtoi(ms[1])
        s = wordtoi(ms[2])
        sum = sum + int(str(f) + str(s))
    else:
        ms = re.search("(\d|one|two|three|four|five|six|seven|eight|nine)", l)
        f = wordtoi(ms[0])
        sum = sum + int(str(f) + str(f))


print(sum)