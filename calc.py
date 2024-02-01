x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
print("1.Add  2.subtract 3.Multiplication 4.Division 5.Modulus")
a=int(input("Enter your choice:"))
if(a==1):
    p=x+y
    print(x,"+",y,"=",p)
elif(a==2):
    p=x-y
    print(x,"-",y,"=",p)
elif(a==3):
    p=x*y
    print(x,"*",y,"=",p)
elif(a==4):
    p=x/y
    print(x,"/",y,"=",p)
elif(a==5):
    p=x%y
    print(x,"%",y,"=",p)
else:
    print("invalid choice,try again")