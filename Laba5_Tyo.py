# 5.	Дана последовательность натуральных чисел A=j=1..n (n<=10000).
# Удалить из последовательности числа , сумма цифр которых кратна 8, а среди оставшихся
# продублировать простые числа
import math
print('Введите массив:')
a = [int(x) for x in input().split()]


def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

i = 0
while i < len(a):
    if a[i] % 8 == 0 and a[i] != 0:
        del a[i]
    else:
        i += 1
i = 0 
while i < len(a):
    if is_prime(a[i]):
        a.insert(i+1, a[i])
        i += 2
print(a)
