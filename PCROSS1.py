test_cases = int(input(""))
l=list()
for i in range(test_cases):
    l.append(input(""))
for i in l:
    m,n,ci,cj = map(int,i.split())
    for i in range(m):
        for j in range(n):
            if j==(cj-1) or i==(ci-1):
                print('*',end='')
            else:
                print('.',end='')
        print('')
