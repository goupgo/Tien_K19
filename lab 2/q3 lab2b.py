def check_Input():
    x = input()
    while True:
        try: x=int(x)
        except:
            x=input()
        else:
            return x
def BIT_Conversion(n):
    lst=[]
    while True:
        if n<=1:
            lst.append(int(n))
            break
        else:
            tmp = int(n%2)
            n/=2
            lst.append(tmp)
    l = len(lst)
    l-=1
    s=''
    while l>=0:
        #print(lst[l])
        s=s+str(lst[l])
        l-=1
    print(s)
def SumOfDigits(n):
    res = 0
    while n>0:
        res+=n%10
        n/=10
        n=int(n)
    return res
def Reverse(n):
    res=0
    while n>0:
        tmp = n%10
        res=res*10+tmp
        n/=10
        n=int(n)
    return res
n=check_Input()
BIT_Conversion(n)
n = int(input())
print(SumOfDigits(n))
print(Reverse(n))