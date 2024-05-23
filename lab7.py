'''
Вариант 22. Сформируйте разные варианты размещения 9 разных монет в 2х карманах.
В первом кармане хранится нечетное количесво монет, в 2 четное
'''
import itertools
import math
from tkinter import *
from tkinter import ttk

itstrs = []
funcstrs = []

coins = ["Монета 1", "Монета 2", "Монета 3", "Монета 4", "Монета 5", "Монета 6", "Монета 7", "Монета 8", "Монета 9"]
coinslen = len(coins)

c = 10

root = Tk()
root.geometry('1200x840')
root.resizable(False, False)

labelc = ttk.Label(text="Количество выводимых вариантов: ")
labelc.place(anchor=NW, x = 30, y = 20, height = 25)
entryc = ttk.Entry()
entryc.place(anchor=NW, x = 250, y = 20, height = 25, width = 80)

labelit = ttk.Label(text="Результат Itertools : ")
labelit.place(anchor=NW, x = 30, y = 60, height = 25, width = 240)

labelal = ttk.Label(text="Результат алгоритма : ")
labelal.place(anchor=NW, x = 30, y = 420, height = 25, width = 240)

def drawScroll():
    itlist = StringVar(value=itstrs)
    listboxd = Listbox(listvariable=itlist)
    listboxd.place(anchor=NW, x=30, y=90, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=90, x=1150, width=20, height=320)
    listboxd["yscrollcommand"] = scrollbar.set

    funclist = StringVar(value=funcstrs)
    listboxt = Listbox(listvariable=funclist)
    listboxt.place(anchor=NW, x=30, y=450, width=1140, height=320)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxt.yview)
    scrollbar.place(anchor=NW, y=450, x=1150, width=20, height=320)
    listboxt["yscrollcommand"] = scrollbar.set


drawScroll()

def shufle(pool, pocket, depth, j):
    global c
    global funcstrs
    if depth == 0:
        if len(pocket) % 2 == 0: return
        if c <= 0: return
        pocket2 = []
        pocket2.extend(pool)
        for i in pocket:
            pocket2.remove(i)

        funcstrs.append('Карман 1 : ')
        for i in pocket:
            funcstrs[-1] += i + ' '
        funcstrs[-1] += ' | Карман 2 : '
        for i in pocket2:
            funcstrs[-1] += i + ' '
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


def main():
    global c
    try:
        c = int(entryc.get())
        cit = int(entryc.get())
    except:
        return

    for i in range(coinslen+1):
        shufle(coins, [], i, 0)

    for i in range(coinslen + 1):
        if cit <= 0: break
        for pocket1 in list(itertools.combinations(coins, i)):
            if len(pocket1) % 2 == 0: continue
            if cit <= 0: break
            pocket2 = []
            pocket2.extend(coins)
            if len(pocket1) > 0:
                for j in pocket1:
                    pocket2.remove(j)
            itstrs.append('Карман 1 : ')
            for i in pocket1:
                itstrs[-1] += str(i) + ' '
            itstrs[-1] += ' | Карман 2 : '
            for i in pocket2:
                itstrs[-1] += str(i) + ' '
            cit -= 1

    drawScroll()


btn = ttk.Button(text="Рассчитать", command=main)
btn.place(anchor=NW, x = 380, y = 20, height = 25, width = 100)

root.mainloop()