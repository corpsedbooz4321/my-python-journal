"""Write a python function to remove a given word from a list and strip it at the same time?"""


def rem(list, word):
    n = []
    for item in list:
        if not (item == word):
            n.append(item.strip(word))
    return n


list = ["aditya", "harry", "shubham", "mahima"]
print(rem(list, "aditya"))
