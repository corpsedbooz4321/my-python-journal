'''write a python program to  rename a file to "renamed_by_python.txt" '''

import os

script = os.path.dirname(os.path.abspath(__file__))

file2 = os.path.join(script, "log5.txt")
file1 = os.path.join(script, "renamed_by_python.txt")


#if os.path.exists(file):
with open(file2, "r") as f:
    content = f.read()
with open(file1, "w") as f:
    f.write(content)
  