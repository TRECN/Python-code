def f(n):
    s=0
    for i in range(1,n+1):
        s+=n%i
    
    return s

l,r=map(int,input().split())

n=l
sum=0;
while n>=l and n<=r:
    if f(n)==f(n-1):
        sum+=n
    n+=1

print(sum)




