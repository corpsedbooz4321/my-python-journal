# import os

# # 1. Get the absolute path to the directory containing this script
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # 2. Join that directory with your filename
# file_path = os.path.join(script_dir, "file.txt")

# # 3. Open the file safely using 'with'
# with open(file_path, "r") as f:
#     data = f.read()
#     print(data)
import os


script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "file.txt")

with open(file_path, "r") as f:
    data = f.read()
    print(data)
    