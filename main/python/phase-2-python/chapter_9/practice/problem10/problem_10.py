'''write program to wipe out the content of a file using python?'''

import os

script = os.path.dirname(os.path.abspath(__file__))

file1 = os.path.join(script, "log4.txt")

if os.path.exists(file1):
    with open(file1, "w") as f:
        f.write("")