'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 22. Сформируйте разные варианты размещения 9 разных монет в 2х карманах.
В первом кармане хранится нечетное количесво монет, в 2 четное
'''
import itertools

def shufle(pool, pocket, depth, j):
    global c
    if depth == 0:
        if len(pocket) % 2 == 0: return
        if c <= 0: return
        pocket2 = []
        pocket2.extend(pool)
        for i in pocket:
            pocket2.remove(i)
        print("Карман 1 : ", *pocket, end='  |  ')
        print("Карман 2 : ", *pocket2)
        c -= 1
        return
    npool = []
    npool.extend(pool)
    for i in pocket:
        npool.remove(i)
    for i in range(j, len(npool) - depth + 1):
        npocket = []
        npocket.extend(pocket)
        npocket.append(npool[i])
        shufle(pool, npocket, depth-1, i)


coins = ["Монета 1", "Монета 2", "Монета 3", "Монета 4", "Монета 5", "Монета 6", "Монета 7", "Монета 8", "Монета 9"]
coinslen = len(coins)

c = int(input("Количество выводимых вариантов : "))
ans = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
if ans == '1':
    print("Результат работы собственное функции")
    for i in range(coinslen+1):
        shufle(coins, [], i, 0)
elif ans == '2':
    print('Результат работы функции itertools')
    for i in range(coinslen+1):
        if c <= 0: break
        for pocket1 in list(itertools.combinations(coins, i)):
            if len(pocket1) % 2 == 0: continue
            if c <= 0: break
            pocket2 = []
            pocket2.extend(coins)
            if len(pocket1) > 0:
                for j in pocket1:
                    pocket2.remove(j)
            print("Карман 1 : ", *pocket1, end='  |  ')
            print("Карман 2 : ", *pocket2)
            c -= 1