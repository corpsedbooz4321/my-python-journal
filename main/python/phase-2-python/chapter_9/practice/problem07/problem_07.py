import os

script = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script, "log2.txt")

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
line_no = 1
for line in lines:
    if "python" in lines:
        print(f"Yes python is present! line: {line_no}")
        break
    line_no += 1
else:
    print("Not found!")

