n1 = int(input(''))
s1 = input('').split()
n2 = int(input(''))
s2 = input('').split()
l1 = [int(i) for i in s1]
l2 = [int(i) for i in s2]
if sum(l1)>sum(l2):
    for i in l1:
        print(i,end=' ')
else:
    for i in l2:
        print(i,end=' ')
