#5.	Дана последовательность натуральных чисел A=j=1..n (n<=10000). 
#Удалить из последовательности числа , сумма цифр которых кратна 8, а среди оставшихся 
#продублировать простые числа 
import math
print('Введите массив:')
a=[int(x) for x in input().split()]


def prost (x):
    k=0
    for i in range(sqrt(x)):
        if x%i==0:
            k+=1
    return(k)

i = 0
while i < len(a):
	if a[i]%8==0 and a[i]!=0:
		del a[i]
	elif prost(a[i])==0:
        a.insert(i+1,a[i])
        i+=2
    else:
        i+=1


print(a)
print()
    



