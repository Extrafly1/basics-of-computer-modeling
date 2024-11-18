# import numpy as np
# import matplotlib.pyplot as plt

# # Определение диапазона значений x1
# x1 = np.linspace(0, 20, 400)

# # Определение ограничений
# # 2 * x1 - 5 * x2 >= -10  => x2 <= (2 * x1 + 10) / 5
# x2_1 = (2 * x1 + 10) / 5

# # 4 * x1 + 5 * x2 <= 40  => x2 <= (40 - 4 * x1) / 5
# x2_2 = (40 - 4 * x1) / 5

# # x1 + 5 * x2 >= 5  => x2 >= (5 - x1) / 5
# x2_3 = (5 - x1) / 5

# # Настройка графика
# plt.figure(figsize=(10, 8))

# # Ограничения
# plt.plot(x1, x2_1, label=r'$2x_1 - 5x_2 \geq -10$', color='blue')
# plt.plot(x1, x2_2, label=r'$4x_1 + 5x_2 \leq 40$', color='red')
# plt.plot(x1, x2_3, label=r'$x_1 + 5x_2 \geq 5$', color='green')

# # Ограничение по неотрицательности
# plt.fill_between(x1, 0, np.maximum(0, np.maximum(x2_3, 0)), where=(x2_1 >= np.maximum(0, np.maximum(x2_3, 0))) & (x2_2 >= np.maximum(0, np.maximum(x2_3, 0))), color='gray', alpha=0.5)

# # Настройки графика
# plt.xlim(0, 20)
# plt.ylim(0, 10)
# plt.xlabel(r'$x_1$')
# plt.ylabel(r'$x_2$')
# plt.axhline(0, color='black', lw=0.5)
# plt.axvline(0, color='black', lw=0.5)
# plt.grid()
# plt.title('Графическое решение задачи линейного программирования')
# plt.legend()
# plt.show()

# # Оптимизация: нахождение угловых точек области допустимых решений
# # В этой области мы можем вручную подставлять точки в функцию цели, чтобы найти максимум и минимум.

# # Определяем угловые точки
# points = [
#     (0, 1),  # Пересечение оси y
#     (5, 0),  # Пересечение с ограничением x1 + 5x2 = 5
#     (10, 0), # Пересечение с ограничением 4x1 + 5x2 = 40
#     (0, 8),  # Пересечение с ограничением 2x1 - 5x2 = -10
# ]

# # Вычисляем значения функции цели для каждой точки
# for x1_val, x2_val in points:
#     z = x1_val + 2 * x2_val
#     print(f"Для точки (x1={x1_val}, x2={x2_val}) значение функции z = {z}")

# решить графически задачу линейного программирования а python:
# z(x) = x1 + 2 * x2  -> max, min.
# {2 * x1 - 5 * x2 >= -10
# {4 * x1 + 5 * x2 <= 40
# {x1 + 5 * x2 >= 5
# {x1 >= 0
# {x2 >= 0

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Определим ограничения и целевую функцию
x1 = np.linspace(0, 15, 400)
x2 = np.linspace(0, 15, 400)

# Условия
y1 = (2 * x1 + 10) / 5  # 2 * x1 - 5 * x2 >= -10 -> x2 <= (2 * x1 + 10) / 5
y2 = (40 - 4 * x1) / 5  # 4 * x1 + 5 * x2 <= 40 -> x2 <= (40 - 4 * x1) / 5
y3 = (5 - x1) / 5       # x1 + 5 * x2 >= 5 -> x2 >= (5 - x1) / 5

# Построим область допустимых значений
plt.figure(figsize=(8, 8))
plt.plot(x1, y1, label='2*x1 - 5*x2 >= -10')
plt.plot(x1, y2, label='4*x1 + 5*x2 <= 40')
plt.plot(x1, y3, label='x1 + 5*x2 >= 5')

# Заштрихуем недопустимые области
plt.fill_between(x1, y1, 15, color='gray', alpha=0.3)  # для первого ограничения
plt.fill_between(x1, y2, 0, color='gray', alpha=0.3)  # для второго ограничения
plt.fill_between(x1, 0, y3, color='gray', alpha=0.3)  # для третьего ограничения

# Ограничения x1, x2 >= 0
plt.xlim(0, 15)
plt.ylim(0, 15)

# Добавим подписи
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Графическое решение задачи линейного программирования')
plt.show()
