import os
import string

BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tree")
os.mkdir(BASE_DIR)

ALPH = string.ascii_lowercase + "_"
FLAG = "uctf_placing_letters_is_very_funny_job"

for sym in ALPH:
    os.mkdir(os.path.join(BASE_DIR, sym))

for i in range(len(FLAG)):
    f = open(os.path.join(BASE_DIR, FLAG[i], str(i + 1)), "w")
    f.close()
