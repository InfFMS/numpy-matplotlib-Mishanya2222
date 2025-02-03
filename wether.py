# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import random
import matplotlib.pyplot
max= 0
maxmax = 0
lst= []
lst2 = []
sr = 0
TF = 0
for i in range(365):
    t = random.randint(-10,35)
    lst.append(t)
    sr = sr + t
    if t > 25:
        TF = TF + 1

for j in lst:
    if j < 0:
        max = max + 1
    else:
        lst2.append(max)
        max = 0

for t in lst2:
    if maxmax < t:
        maxmax = t
print('Самая длинная последовательность дней, когда температура была ниже 0:',maxmax, '\n\nКоличество дней с температурой выше 25:', TF )
r = 0
categ = [ ]
for l in range(365):
    r =r +1
    categ.append(r)
mn = 0
categ2= []
val2=[]
for ij in lst:
    mn = mn + 1
    if ij == -10:
        val2.append(ij)
        categ2.append(mn)
val3 = []
categ3 = []
nm = 0
for ji in lst:
    nm =nm +1
    if ji == 35:
        val3.append(ji)
        categ3.append(nm)

matplotlib.pyplot.plot(categ, lst)
matplotlib.pyplot.plot(categ2, val2, 'o-b' )
matplotlib.pyplot.plot(categ3,val3, 'o-r')
matplotlib.pyplot.show()
print(categ2)

# я понял, что под 'теплыми' днями подразумевются дни с температурой 35 градусов, а под 'холодными' с температурой -10 градусов)