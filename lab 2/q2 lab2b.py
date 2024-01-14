import math
def GCD(n,m):
    while m!=0:
        tmp = m
        m=n%m
        n=tmp
    return n
def LCM(n,m):
    tmp = GCD(n,m)
    return int(n*m/tmp)
n = int(input())
m = int(input())
if n>m:
    swap(n,m)
tmp = int(math.sqrt(m))
for i in range(2,tmp):
    if n%i==0 and m%i==0:
        print(i)
print(GCD(n,m))
print(LCM(n,m))