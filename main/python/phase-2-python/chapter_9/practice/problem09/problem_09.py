'''Write a program to find out whether a file is identical & matches the content of another file.'''

import os

script = os.path.dirname(os.path.abspath(__file__))
path_file = os.path.join(script, "1st.txt")
another_file = os.path.join(script, "2nd.txt")


if os.path.exists(path_file):#takes the content from the joined file "1st.txt"
    with open(path_file, "r") as f:
        data1 = f.read()#stores the sotres the content of the file 1st.txt in variable data1.
   
#if os.path.exists(another_file):
    with open(another_file, "r") as f:
        data2 = f.read()
    
if data1 == data2:
    print("file found with identical contents in it!")
else:
    print("Nothings wrong! files no files are found with same contents in it!")