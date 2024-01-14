n = int(input())
mx = 0
for i in range(0,n):
    tmp = int(input())
    if tmp > mx:
        mx = tmp
print(mx)