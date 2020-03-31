test_cases = int(input(""))
l=list()
for i in range(test_cases):
    l.append(input(""))
for i in l:
    m,n,ci,cj = map(int,i.split())
    ci = ci-1
    cj=cj-1
    for i in range(m):
        for j in range(n):
            if abs(ci-i) == abs(cj-j):
                print('*',end='')
            else:
                print('.',end='')
        print('')
