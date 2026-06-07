#if you want to use this code, you have to comment out the one of the both versions.


temp = float(input("Enter the hours: "))
pemp = float(input("Enter rate per hour: "))

#first version
print(temp,pemp)
if temp > 40:
    print("overtime")
    reg = pemp*40
    otp = (temp - 40) * (pemp*1.5)
    xx = otp + reg
else:
    print("regular")
    xx = temp*pemp
print("Pay:", xx)

#second version
if temp < 40:
    xx = temp * pemp
    print(xx)
else:
    xx = (temp - 40) * pemp*1.5 + pemp*40
    print(xx)
