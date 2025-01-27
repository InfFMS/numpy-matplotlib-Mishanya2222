# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
ch = [1,0]

for i in range(8):
    if i % 2== 0:
        print("01010101")
    else:
        print("10101010")




dx, dy = 0.1, 0.1
P = np.arange(-5.0, 5.0, dx)
Q = np.arange(-5.0, 5.0, dy)
P, Q = np.meshgrid(P, Q)



min_max = np.min(P), np.max(P), np.min(Q), np.max(Q)
res = np.add.outer(range(8), range(8)) %2
cmap = colors.ListedColormap(['white','red','black'])
norm = colors.BoundaryNorm(res)
plt.imshow(res, cmap=cmap, norm=norm )
plt.show()