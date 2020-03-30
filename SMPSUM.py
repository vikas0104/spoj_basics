a,b = map(int,input().split())
s=0
for i in range(a,b+1):
    s=i*i+s
print(s)
