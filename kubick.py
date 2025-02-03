# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import random
import matplotlib.pyplot
lst =[[],[],[],[],[],[]]
for i in range(1,1000):
    t = random.randint(1,6)
    lst[t-1].append(t)
val = [len(lst[0]),len(lst[1]),len(lst[2]),len(lst[3]), len(lst[4]), len(lst[5])]
categ = ["1","2","3","4","5","6"]

matplotlib.pyplot.bar(categ, val)
matplotlib.pyplot.show()