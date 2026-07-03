'''write a python program to wipe the contents of a file?'''

import os

script = os.path.dirname(os.path.abspath(__file__))

file = os.path.join(script, "log4.txt")

if os.path.exists(file):
    with open(file, "w") as f:
        f.write("")