n=int(input(''))
moon = input('').split()
for i in range(n):
    moon[i]=int(moon[i])
for i in range(1):
    if len(moon)==1:
        print('-1')
        break
    if moon[len(moon)-2]>moon[len(moon)-1]:
        print('MENGUANTE')
    else:
        print('CRECIENTE')
