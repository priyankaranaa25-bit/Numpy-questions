print("1-addition")
print("2-substraction")
print("3-multiplication")
print("4-division")
option =int(input("choose an operation:"))

result=0
if(option in[1,2,3,4]):
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

if(option==1):
          result=num1+num2
          print("result=num1+num2")
elif(option==2):
          result=num1-num2
          print("result=num1-num2")
elif(option==3):
          result=num1*num2
          print("result=num1*num2")
elif(option==4):
        result=num1/num2
        print("result=num1/num2")
else:
        print("invalid operation entered")

print("the result of the operation is {}".format(result))