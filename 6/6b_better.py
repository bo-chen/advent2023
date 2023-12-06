import math
import numpy as np
import os
import re
import sys
from functools import reduce
from pathlib import Path

t = 51699878
d = 377117112241505

print(math.ceil(math.sqrt(t*t - 4*d)))