def Reverse(n):
    res=0
    while n>0:
        tmp = n%10
        res=res*10+tmp
        n/=10
        n=int(n)
    return res
n = int(input())
m = int(input())
for i in range(n,m):
    if i == Reverse(i):
        print(i)