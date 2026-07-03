'''write a python program to  rename a file to "renamed_by_python.txt"'''

import os

script = os.path.dirname(os.path.abspath(__file__))

file = os.path.join(script, "log5.txt")


#if os.path.exists(file):
with open(file, "r") as f:
    content = f.read()
with open("renamed_by_python.txt", "w") as f:
    f.write(content)
  