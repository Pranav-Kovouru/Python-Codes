a,b,c,d=map(int,input("Enter 4 numbers : ").split())
if (a>b and a>c and a>d ):
    print(f"{a} is greatest number ")
elif (b>a and b>c and b>d ):
    print(f"{b} is greatest number ")
elif (c>a and c>b and c>d ):
    print(f"{c} is greatest number ")
elif (d>a and d>b and d>c ):    
    print(f"{d} is greatest number ")



if (a>b):
    maxnum1=a 
else :
    maxnum1 = b
if (c>d):
    maxnum2 = c
else :
    maxnum2 = d
if (maxnum1>maxnum2):
    print(f"{maxnum1} is greatest")      
else:
    print(f"{maxnum2} is greatest")            