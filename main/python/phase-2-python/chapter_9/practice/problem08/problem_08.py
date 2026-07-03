'''write a program to make a copy of a text file "this.txt"'''

import os

script = os.path.dirname(os.path.abspath(__file__))
path_file = os.path.join(script, "log3.txt")
another_file = os.path.join(script, "this.txt")

if os.path.exists(path_file):
    with open(path_file, "r") as f:
        content = f.read()
        
    with open(another_file, "w") as f:
        f.write(content)
        

