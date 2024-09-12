#armstrong 
a=int(input("enter the number: "))
sum=0
temp=a
while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
if a==sum:
     print("armstromg")
else:
     print("not")
