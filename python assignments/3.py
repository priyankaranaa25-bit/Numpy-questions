a=int(input("enter first number"))
b=int(input("enter second number"))
t1,t2=a,b
while b>0:
    r=a%b
    a=b
    b=r
    gcd=a
    lcm=(t1*t2)/gcd
    print ("gcd is",gcd)
    print("lcm is",lcm)