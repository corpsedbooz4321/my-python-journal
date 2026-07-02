'''write a program to mine a log file and find out whether it contains "python"'''

import os

script = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script, "log.txt")


if os.path.exists(file_path):
    with open(file_path, "r") as f:
         data = f.read()
         user = input('enter the word you want to find in the log file: ')
         user = bool(user)
         if "python" in data:
            print(f'Found!')
         else:
            print('not found!')



