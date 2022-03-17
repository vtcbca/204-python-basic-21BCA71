#was to enter 3 number and check which number is maximum

a=int(input("Enter Any Number:"))
b=int(input("Enter Any Number:"))
c=int(input("Enter Any Number:"))
if((a>b)and(a>c)):
    print("{} is a maximum number".format(a))
elif((b>a)and(b>c)):
    print("{} is a maximum number".format(b))
elif((c>a)and(c>b)):
    print("{} is a maximum number".format(c))
