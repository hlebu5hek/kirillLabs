#Вариант 22. Натуральные числа, начинающиеся с нечетной цифры и содержащие не более 2 четных цифр.
#Для каждого числа через тире вывести прописью первую цифру и четные цифры.
#Исопльзовать re
import re
def checkNum(str_num):
    if re.match("^[02468]+$", str_num[0]): return False
    if len(str_num) - len(re.sub(r"[24680]", '', str_num)) > 2: return False
    return True

nums = []
file_name = "text.txt"
perev_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три',
              '4': 'четыре', '5': 'пять', '6': 'шесть',
              '7': 'семь', '8': 'восемь', '9': 'девять'}
try:
  open(file_name, "r")
except:
  print("Файл отсутствует")

with open(file_name, "r") as file:
  for line in file.readlines():
    line = line.replace('\n', '')
    if not re.match("^[0-9]+$", line): continue
    if(checkNum(line)):
        print("Подходящее число : ", line)
        even = re.sub(r"[13579]", '', line)
        print(perev_cifr[line[0]], " ; ", *list(map(lambda x: perev_cifr[x], even)), '\n')