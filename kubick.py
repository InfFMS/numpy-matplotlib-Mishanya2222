# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import random
import matplotlib.pyplot
lst3=[]
lst2  = []
lst =[[],[],[],[],[],[]]
for i in range(1,1000):
    t = random.randint(1,6)
    lst[t-1].append(t)
    lst2.append(t)
val = [len(lst[0]),len(lst[1]),len(lst[2]),len(lst[3]), len(lst[4]), len(lst[5])]
categ = ["1","2","3","4","5","6"]


max = 0
lengt = 0
for j in lst2:
    if j == max:
        lengt = lengt + 1

    else:
        lst3.append(lengt)
        max = j
        lengt=1


maxmax = 0
for r in lst3:
    if maxmax < r:
        maxmax = r
print(maxmax)

matplotlib.pyplot.bar(categ, val)
matplotlib.pyplot.show()



#вероятность выпадения каждого значения 1/6
