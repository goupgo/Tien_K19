def Reverse(n):
    res=0
    while n>0:
        tmp = n%10
        res=res*10+tmp
        n/=10
        n=int(n)
    return res
n = int(input('original number'))
if n == Reverse(n):
    print('Given number is palindrome')
else:
    print('Given number is not palindrome')