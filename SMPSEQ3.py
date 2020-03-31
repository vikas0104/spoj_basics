s1 = int(input(""))
a = input("").split()
s2 = int(input(""))
b = input("").split()
for i in range(s1):
    if a[i] not in b:
        print(a[i]+" ",end='')
