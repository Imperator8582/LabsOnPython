a=[]
print('Введите n')
n=int(input())
print('Введите числа')

for i in range (n):
    a.append([int(j) for j in input().split()])  
maxim=-1000000

for j in range (len(a[i])):
    summa=0
    for i in range(n):
        summa=summa+a[i][j]
    if summa > maxim:
        maxim=summa  
              
print('Наибольшая сумма эелемнтов столбцов= ', maxim)


