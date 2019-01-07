# 4.	Дана целочисленная матрица A=i..n, j=..m (n,m<=100). Найти столбец с наибольшим произведением 
# элементов и заменить все элементы этого столбца этим произведением
a=[]
print('Введите размерность матрицы:')
n=int(input())

print('Введите числа')

for i in range (n):
    a.append([int(j) for j in input().split()]) 

k=1
maxim=-99999999
js=-1
 
for j in range (len(a[i])):
    k=1
    for i in range (n):
        k=k*a[i][j]
    if k>maxim:
        maxim=k
        js=j

for i in range (n):
    for j in range (len(a[i])):
        if j==js:
            a[i][j]=maxim
print()

for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()



