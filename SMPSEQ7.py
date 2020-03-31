# i am sure there must be a better approach to solve this problem but for now i did get the concept...and thats it..!!
n = int(input(""))
s = input("").split()
cm = 0
cd = 0
for i in range(n):
    ar1 = s[:i]
    ar2 = s[i:]
    t1 = s[:i]
    t2 = s[i:]
    if len(ar1)<=1 or len(ar2)<=1:
        continue
    ar1.sort(key=int,reverse=True)
    ar2.sort(key=int)
    if ar1==t1 and ar2==t2:
        print(ar1)
        print(t1)
        print(ar2)
        print(t2)
        cm+=1
        for i in range(len(ar1)):
            for j in range(i+1,len(ar1)):
                if ar1[i]==ar1[j]:
                    cd+=1
if cm!=cd:
    print('Yes')
else:
    print('No')
