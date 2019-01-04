# 3. Дана последовательность натуральных чисел A=j=1..n (n<=10000)
# Если в последовательности нетдвух одинаковых чисел, упорядочить последовательность по 
# убыванию последней цифры числa */
print('Введите массив')

a= [int(x) for x in input().split()]
b=False
n=1

if len(a)> len(set(a)):
    b=True
#while n<len(a):
#    for i in range (len(a)-n):
#        if a[i]==a[i+1]:
#            b=b+1
 #   n=n+1

if b==True:
    while n<len(a):
        for i in range (len(a)-n):
            if a[i]%10 > a[i+1]%10 :
                a[i],a[i+1]=a[i+1],a[i]
        n=n+1

print(a)