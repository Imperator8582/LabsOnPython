#2.	Введите последовательность натуральных чисел A=j=1..n (n<=1000)упорядочить последовательность 
# по возрастанию наибольшей цифры числа, числа с одинаковыми наибольшими цифрами дополнительно упорядочить
#  по возрастанию произведения цифр числа , числа с одинаковыми наибольшими цифрами и произведением цифр
#  дополнительно упорядочить по возрастанию самого числа

print('Введите элементы: ')

a = [int(x) for x in input().split()]
def ProizvOfNumber (a):
    k=1
    while a>0:
        b=a%10
        a=a//10
        k=k*b
    return k

def MaxNumber (a):
    maxi=-1
    while(a>0):
        b=a%10
        a=a//10
        if b > maxi:
            maxi=b
    return maxi

n=1
while n<len(a):
    for i in range (len(a)-n):
        if MaxNumber(a[i]) > MaxNumber(a[i+1]):
           a[i],a[i+1]=a[i+1],a[i]
        else:
            if MaxNumber(a[i])==MaxNumber(a[i+1]):
                if ProizvOfNumber(a[i]) > ProizvOfNumber(a[i+1]):
                       a[i],a[i+1]=a[i+1],a[i]
                if ProizvOfNumber(a[i])== ProizvOfNumber(a[i+1]):
                    if a[i]>a[i+1]:
                        a[i],a[i+1]=a[i+1],a[i]
    n=n+1

print(a)
                    
                    



