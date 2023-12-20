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
# s3 txt to give 3
with open(f'{source_dir}/in.txt') as fp:
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


countp = {"l": 0, "h":0}

def sendsig(f, c, sig):
    ps = []
    for o in c["o"]:
        ps.append([o, f, sig])
        if sig == "l":
            countp["l"] += 1
        else:
            countp["h"] += 1

    return ps

presses = 0
keycomps = ["fk", "rz", "lf", "br"]
keyrepeats = {}

# ps : [name, from, sig]
def step(states, ps):
    n, f, sig = ps[0]

    if sig == 'h' and f in keycomps and f not in keyrepeats:
        keyrepeats[f] = presses
        if len(keyrepeats) == len(keycomps):
            prod = math.lcm(*keyrepeats.values())
            print(prod)
            exit()
    
    if n == "rx":
        return ps[1:]

    c = comps[n]
    nps = []
    if c["t"] == "b":
        nps = sendsig(n, c, sig)
    elif c["t"] == "%":
        if sig == "l":
            states[n] = not states[n]
            if states[n]:
                nps = sendsig(n, c, "h")
            else:
                nps = sendsig(n, c, "l")
    elif c["t"] == "&":
        states[n][f] = sig
        allh = True
        for v in states[n].values():
            if v == "l":
                allh = False
        if allh:
            nps = sendsig(n, c, "l")
        else:
            nps = sendsig(n, c, "h")
    
    return ps[1:] + nps


def inits():
    states = {}
    for n in comps:
        c = comps[n]
        if c["t"] == "%":
            states[n] = False
        if c["t"] == "&":
            mem = {}
            for n2 in comps:
                c2 = comps[n2]
                for o in c2["o"]:
                    if o == n:
                        mem[n2] = "l"
            states[n] = mem

    return states

def press(states):
    ps = [["broadcaster", "button", "l"]]
    countp["l"] += 1
    while ps != []:
        ps = step(states, ps)

states = inits()
while True:
    presses += 1
    press(states)