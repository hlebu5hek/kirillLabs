'''Вариант 22
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.
d e
c b
 4
3 1
 2
Формируется матрица F следующим образом:
если в С сумма чисел, по периметру области 3 больше, чем произведение чисел по периметру области 2,
то поменять в С симметрично области 2 и 3 местами, иначе В и Е поменять местами несимметрично.
При этом матрица А не меняется.
После чего вычисляется выражение: A*F+ K*FT .
'''

from random import randint as rnd

def printList(z):
    for i in z:
        for j in i:
            print("{:5}".format(j), end=' ')
        print()
    print()

k, n = int(input("k = ")), int(input("n = "))
m = n//2
n = m*2
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(rnd(-10,10))

print("Матрица A : ")
printList(a)

b = []
c = []
d = []
e = []
for i in range(m):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(m):
        b[i].append(a[i+m][j+m])
        c[i].append(a[i+m][j])
        d[i].append(a[i][j])
        e[i].append(a[i][j+m])

print("Матрица B : ")
printList(b)
print("Матрица C : ")
printList(c)
print("Матрица D : ")
printList(d)
print("Матрица E : ")
printList(e)

summ_ = 0
summ_ += c[0][0] #первый угол
summ_ += c[m-1][0] #второй угол
for i in range(1, m//2):
    for j in [0, i]:
        summ_ += c[i][j]
for i in range(m // 2, m-1):
    for j in [0, m-i-1]:
        summ_ += c[i][j]
print("B С сумма чисел, по периметру области 3 =", summ_)

mult_ = 1
mult_ *= c[m-1][0] #первый угол
mult_ *= c[m-1][m-1] #второй угол
for j in range(1, m//2):
    for i in [m-1, m-j-1]:
        mult_ *= c[i][j]
for j in range(m//2, m-1):
    for i in [j, m-1]:
        mult_ *= c[i][j]
print("В С произведение чисел по периметру области 2 =", mult_)

if summ_ > mult_:
    print("Сумма чисел больше произведения\n")
    for i in range(0, m//2):
        for j in range(0, i+1):
            c[i][j], c[m-j-1][m-i-1] = c[m-j-1][m-i-1], c[i][j]
    for i in range(m//2, m):
        for j in range(0, m-i):
            c[i][j], c[m-j-1][m-i-1] = c[m-j-1][m-i-1], c[i][j]
else:
    print("Сумма чисел меньше произведения\n")
    for i in range(m):
        for j in range(m):
            b[i][j], e[i][j] = e[i][j], b[i][j]

print("Матрица B : ")
printList(b)
print("Матрица C : ")
printList(c)
print("Матрица D : ")
printList(d)
print("Матрица E : ")
printList(e)

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(e[i])
for i in range(m, n):
    f[i].extend(b[i-m])

print("Матрица F : ")
printList(f)

ft = []

for i in range(n):
    ft.append([])
    for j in range(n):
        ft[i].append(f[j][i])

print("Матрица F трансп. : ")
printList(ft)

fk = []
for i in range(n):
    fk.append([])
    for j in range(n):
        fk[i].append(ft[i][j] * k)

print("Матрица FT умноженная на K : ")
printList(fk)

fa = []

for i in range(n):
    fa.append([])
    for j in range(n):
        s = 0
        for l in range(n):
             s += f[i][l]*a[j][l]
        fa[i].append(s)

print("Матрица F умноженная на A : ")
printList(fa)

for i in range(n):
    for j in range(n):
        ft[i][j] += fa[i][j]

print("A*F + K*FT : ")
printList(ft)
