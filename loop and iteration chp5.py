

# num = float(input("Enter the decend number: "))


# n = num
# while n > 0:  
#   print("blast off")


while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("done")