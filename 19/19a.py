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

ws = {}
def parsew(s):
    m = re.search("^(\w+).(.*).$", s)
    name = m[1]
    rstrs = m[2].split(",")
    rules = []
    lastrule = {"iscond": False, "input":"", "cond":"", 
                "const":0, "output": rstrs[-1]}
    rstrs = rstrs[:-1]
    for rs in rstrs: 
        m = re.search("(^\w+)(.)(\d+):(\w+)$", rs)
        rules.append({"iscond": True, "input":m[1], "cond":m[2], 
                "const":int(m[3]), "output": m[4]})

    rules.append(lastrule)
    ws[name] = rules

parts = []
def parsep(s):
    s = s[1:-1]
    varstrs = s.split(",")
    part = {}
    for v in varstrs:
        n, x = v.split("=")
        part[n] = int(x)
    parts.append(part)

with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()
        if lstripped == "":
            break

        parsew(lstripped)

    for line in fp:
        lstripped = line.strip()
        if lstripped != "":
            parsep(lstripped)

def procrule(w, part):
    # rules.append({"iscond": True, "input":m[1], "cond":m[2], 
    #    "const":int(m[3]), "output": m[4]})
    for r in w:
        o = r["output"]
        if r["iscond"] == False:
            if o in ["A", "R"]:
                return o
            return procrule(ws[o], part)
        i = part[r["input"]]
        cond = r["cond"]
        cons = r["const"]
        if cond == ">" and i > cons:
            if o in ["A", "R"]:
                return o
            return procrule(ws[o], part)
        elif cond == "<" and i < cons:
            if o in ["A", "R"]:
                return o
            return procrule(ws[o], part)

    return None

total = 0
for p in parts:
    rres = procrule(ws["in"], p) 
    if rres == "A":
        total += sum(p.values())

    elif rres != "R":
        print("Bad")

print(total)


            
        