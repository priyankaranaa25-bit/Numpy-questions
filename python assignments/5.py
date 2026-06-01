str1=input("enter string1")
str2=input("enter string2")
if len(str1)!=len(str2):
    print("not anagrams")
else:
    if sorted(str1)==sorted(str2):
        print("strings are anagrams")
    else:
        print("not anagrams")