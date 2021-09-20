n=int(input())
c=1;
for i in range(1,n):
    if n%i==0:
        c+=1

if(c==2):
    print("prime")
else:
    print("not prime")
