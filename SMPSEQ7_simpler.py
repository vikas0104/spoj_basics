n = int(input(""))
ar = input('').split()
a=list()
for i in range(len(ar)):
    a.append(int(ar[i]))
#print(a)
count=0

for i in range(len(a)):
    if a[i]>a[i+1]:
        count=count+1
    else:
        break
count=count+1
for j in range(count,len(a)-1):
    if a[j]<a[j+1]:
        count=count+1
    else:
        break
count=count+1
if count==len(a):
    print('Yes')
else:
    print('No')
