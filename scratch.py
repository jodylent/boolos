import os
import sys
sys.path.append("/Users/jlent/Dropbox/scripts")
from hardest_logic_puzzle import *

pantheon = [T_God(), F_God(), R_God()]
pantheon_dict = {
    "T": pantheon[0],
    "F": pantheon[1],
    "R": pantheon[2],
}

random.shuffle(pantheon)

a = pantheon[0]
b = pantheon[1]
c = pantheon[2]

pantheon_dict["a"] = a
pantheon_dict["b"] = b
pantheon_dict["c"] = c

q = "isinstance(self, F_God)"




# >>> b.answer("isinstance(pantheon_dict['b'], F_God)", pantheon_dict)
a.answer(q)