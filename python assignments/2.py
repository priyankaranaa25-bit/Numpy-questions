print("create your account:")
un=input("username:")
pw=input("password:")
print ("\n\n======\n\n")
u=input("what is your username?\n")
if u==un:
    p=input("password?\n")
    if p==pw:
        print("correct")
    else:
        print("incorrect")
else:
    print("username entered is not correct")