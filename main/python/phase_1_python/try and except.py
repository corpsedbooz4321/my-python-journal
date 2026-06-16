tep = "hello world"
try:
    tep = int(tep)
except:istr = -1

print("first", tep)
tep = "123"
try:
    tep = int(tep)
except:
    tep = -1
print("second", tep)

#second topic of practice

temp = input("Enter: ")
try:
    temp = int(temp)
    print("done")
except:
    temp = -1
if temp > 0:
    print("NICE JOB")
else:
    print("not a number!")