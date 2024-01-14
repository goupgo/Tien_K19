import math
def check():
    x = int(input())
    while x<5:
        x=int(input())
    return x
def Q_02(n):
    S1 = n*(n+1)/2
    return S1
def Q_03(n):
    res = 1
    for i in range(1,n):
        res*=i
    return res
def Q_04(n):
    res = 0
    for i in range(1,n):
        res+=1/n
    return res
def Q_05():
    x=int(input())
    tmp = int(math.sqrt(x))
    for i in range(2,tmp):
        if x%i==0:
            return False
    return True
n = check()
S1 = Q_02(n)
S2 = Q_03(n)
S3 = Q_04(n)
S4 = Q_05(n)