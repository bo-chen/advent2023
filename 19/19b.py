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

with open(f'{source_dir}/in.txt') as fp:
    for line in fp:
        lstripped = line.strip()
        if lstripped == "":
            break

        parsew(lstripped)

avs = []
def procrule(w, vs):
    # rules.append({"iscond": True, "input":m[1], "cond":m[2], 
    #    "const":int(m[3]), "output": m[4]})
    for r in w:
        o = r["output"]
        if r["iscond"] == False:
            if o == "A":
                avs.append(vs)
                return
            if o == "R":
                return
            return procrule(ws[o], vs)
        i = r["input"]
        cond = r["cond"]
        cons = r["const"]
        if cond == ">":
            if vs[i][1] <= cons:
                 continue
            nvs = copy.deepcopy(vs)
            nvs[i][0] = cons + 1
            vs[i][1] = cons
            if o == "A":
                avs.append(nvs)
            elif o != "R":
                procrule(ws[o], nvs)
        elif cond == "<":
            if vs[i][0] >= cons:
                 continue
            nvs = copy.deepcopy(vs)
            nvs[i][1] = cons - 1
            vs[i][0] = cons
            if o == "A":
                avs.append(nvs)
            elif o != "R":
                procrule(ws[o], nvs)

    return None

procrule(ws["in"], {"x":[1,4000],"m":[1,4000], "a":[1,4000],"s":[1,4000]})

total = 0
for vs in avs:
    prod = 1
    for i in ["x", "m", "a", "s"]:
        if vs[i][1] < vs[i][0]:
            print("bad")
        prod *= vs[i][1] - vs[i][0] + 1
    total += prod

print(total)