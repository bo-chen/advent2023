import math
import numpy as np
import os
import re
import sys
import copy
import functools as ft
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
# s3 txt to give 3
with open(f'{source_dir}/s3.txt') as fp:
    for line in fp:
        lstripped = line.strip()

        if lstripped != "":
            ls.append(lstripped)

comps = {}
for l in ls:
    m = re.search("^(.+) -> (.+)$", l)
    t = None
    n = None
    if m[1] == "broadcaster":
        t = "b"
        n = m[1]
    else:
        t = m[1][0]
        n = m[1][1:]
    
    comps[n] = {"t" :t, "o": m[2].split(", ")}


inputs = {}
for n in comps:
    c = comps[n]
    mem = {}
    for n2 in comps:
        c2 = comps[n2]
        for o in c2["o"]:
            if o == n:
                mem[n2] = "l"
    inputs[n] = mem

# returns [period, first]
@ft.cache
def whensig(n, sig):
    c = comps[n]
    t = c["t"]
    if t == "b":
        if sig == "l":
            return [1, 0]
        if sig == "h":
            print("bad")
            exit()
    if t == "%":
        inp, inf = whensig(inputs[n][0], "l")
        if sig == "h":
            return [2 * inp, inf]
        else:
            return [2 * inp, inf + inp]
    if t == "&":
        if sig == "h":
            minp = -1
            minf = -1
            for input in inputs[n]:
                inp, inf = whensig(input, "l")
                if minp == -1 or inp < minp:
                    minp = inp
                    minf = inf
                if inp == minp and inf < minf:
                    minf = inf
                inp, inf = whensig(input, "h")
                if minp == -1 or inp <= minp:
                    minp = inp
                    minf = inf
                if inp == minp and inf < minf:
                    minf = inf
            return [minp, minf]
        if sig == "l":







            

def 


while True:
    presses += 1
    press(states)

print(countp["l"] * countp["h"])